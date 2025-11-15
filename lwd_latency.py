#!/usr/bin/env python3
import time
import socket

LIGHTWALLETD_SERVERS = [
    ("mainnet.lightwalletd.com", 9067),
    ("lightd-main.z.cash", 9067),
    # Weitere Endpunkte später ergänzen
]

TIMEOUT = 3.0  # Sekunden
REPEAT = 3     # Anzahl Messungen pro Server


def measure_latency(host, port, timeout=TIMEOUT):
    latencies = []
    for _ in range(REPEAT):
        start = time.time()
        try:
            with socket.create_connection((host, port), timeout=timeout):
                elapsed = (time.time() - start) * 1000.0  # ms
                latencies.append(elapsed)
        except socket.gaierror:
            # DNS-Problem: Hostname kann nicht aufgelöst werden
            return None, "dns_error"
        except socket.timeout:
            latencies.append(None)
        except OSError:
            latencies.append(None)
    return latencies, None


def main():
    print("Zcash Lightwalletd Latency Checker")
    print("---------------------------------")
    for host, port in LIGHTWALLETD_SERVERS:
        print(f"\nTesting {host}:{port} ...")
        latencies, error = measure_latency(host, port)
        if error == "dns_error":
            print("  ❌ DNS error: hostname could not be resolved")
            continue
        if not latencies or all(l is None for l in latencies):
            print("  ❌ No response (all attempts failed)")
            continue
        valid = [l for l in latencies if l is not None]
        avg = sum(valid) / len(valid)
        print(f"  Measurements: {['%.1f ms' % l if l is not None else 'timeout' for l in latencies]}")
        print(f"  ➜ Average: {avg:.1f} ms")


if __name__ == "__main__":
    main()

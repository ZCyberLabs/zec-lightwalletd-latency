# Zcash Lightwalletd Latency Checker

A small Python CLI tool to measure TCP connection latency to one or more Zcash lightwalletd servers.

It is intended for node operators, wallet developers and researchers who want to compare lightwalletd endpoints by simple connection time.

---

## Features

- Tests connectivity to a list of lightwalletd endpoints (host:port)
- Performs multiple connection attempts per host
- Reports:
  - Individual measurements (in milliseconds, or `timeout`)
  - Average latency for successful attempts
- Distinguishes between:
  - DNS errors (hostname cannot be resolved)
  - Connection timeouts

---

## Current Limitations

- Uses raw TCP connections (no gRPC protocol-level checks yet)
- Does not validate TLS certificates
- Does not verify that the remote service is actually a lightwalletd instance
- Endpoint list is currently hardcoded in the script

Future versions may support:

- Configurable endpoint lists (via config file or CLI)
- JSON output for integration into monitoring systems
- gRPC-level health checks

---

## Requirements

- Python 3.8 or newer
- No external Python dependencies (uses only the standard library)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ZCyberLabs/zec-lightwalletd-latency.git
cd zec-lightwalletd-latency

(Optional) create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate


Usage

Run the latency checker:

python3 lwd_latency.py


By default, the script contains a list of lightwalletd endpoints like:
LIGHTWALLETD_SERVERS = [
    ("mainnet.lightwalletd.com", 9067),
    ("lightd-main.z.cash", 9067),
    # add more endpoints here
]


You can edit this list directly in lwd_latency.py to test your own endpoints, for example:

LIGHTWALLETD_SERVERS = [
    ("my-lightwalletd.example.org", 9067),
]


LIGHTWALLETD_SERVERS = [
    ("my-lightwalletd.example.org", 9067),
]

Interpreting the output

DNS error: the hostname cannot be resolved in your current network (possible DNS or firewall issue)

timeout: TCP connection could not be established within the configured timeout

XX.X ms: successful connection with measured latency

Roadmap

Make endpoint list configurable via CLI and/or config file

Add JSON output mode

Add gRPC health checks against lightwalletd

Add basic statistics (min, max, median)

Optional Prometheus exporter mode

Better error messages and logging

License

MIT License
See the LICENSE file for full details (to be added).

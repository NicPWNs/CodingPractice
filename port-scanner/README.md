# Port Scanner

## Usage
```bash
python3 port-scanner.py <TARGET> <PORTS>
```
## Arguments
### \<TARGET\>
Hostname or IP Address

### \<PORTS\>
Specify:
1. "common" - Will scan ports 1-1024
2. "all" - Will scan all ports 1-65535

## Test
Test this with my [port scan detector](../port-scan-detector).

## To Do
- [ ] Add CLI arguments to specify ports to scan.
- [ ] Add support for scanning a network range.
- [ ] Add support for stealthy scans (SYN Stealth).
- [ ] Improve error handling.

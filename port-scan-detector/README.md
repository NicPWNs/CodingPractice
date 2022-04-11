# Port Scan Detector

## Usage
```bash
python3 port-scan-detector.py
```

## Behavior
Listens on port 1023/tcp for connections, by default.

## Test
Test this with my [port scanner](../port-scanner).

## To Do
- [ ] Detect based on # of strange ports connected to.
- [ ] Detect based on sequential ports connected to.
- [ ] Add CLI arguments to toggle modes of detection.
- [ ] Detect stealthy scans (SYN Stealth).

## Internet Health Monitor (Python)

Simple CLI that pings your configured endpoints and prints current latency.

### Quick start
- Install dependencies:

```bash
pip install -r requirements.txt
```

- Configure endpoints in `settings.py`.

- Run (every 30s, default timeout 2s):

```bash
py main.py 30
```

Optional timeout:

```bash
py main.py 30 --timeout 3
```

Press Ctrl+C to stop.

### Notes
- Windows: ICMP may require running the terminal as Administrator.
- Some hosts/CDNs drop ICMP; occasional "timeout" can be normal even if HTTPS works.
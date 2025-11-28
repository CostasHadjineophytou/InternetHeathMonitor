import argparse
import sys
import time
from datetime import datetime

from internet_monitor import InternetMonitor


def _positive_float(value: str) -> float:
	try:
		parsed = float(value)
	except ValueError as exc:
		raise argparse.ArgumentTypeError(f"Invalid number: {value}") from exc
	if parsed <= 0:
		raise argparse.ArgumentTypeError("Value must be greater than 0")
	return parsed


def main() -> None:
	parser = argparse.ArgumentParser(description="Internet health monitor that periodically pings configured endpoints.")
	parser.add_argument("interval", type=_positive_float, help="Seconds between checks (e.g., 30)")
	parser.add_argument("--timeout", type=_positive_float, default=2.0, help="Per-ping timeout in seconds (default: 2)")
	args = parser.parse_args()

	try:
		from settings import ENDPOINTS
		monitor = InternetMonitor(endpoints=ENDPOINTS)
	except Exception as e:
		print(f"Failed to load settings or initialize monitor: {e}", file=sys.stderr)
		raise SystemExit(1)

	try:
		while True:
			now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			print(f"\n[{now}] Internet health check (interval: {args.interval}s, timeout: {args.timeout}s)")
			results = monitor.get_current_latency(timeout=args.timeout)
			for name, latency_ms in results.items():
				status = f"{latency_ms:.2f} ms" if latency_ms is not None else "timeout"
				print(f"- {name}: {status}")
			time.sleep(args.interval)
	except KeyboardInterrupt:
		print("\nStopped internet health monitor.")


if __name__ == "__main__":
	main()



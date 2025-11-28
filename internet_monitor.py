from typing import Dict, Optional

from ping3 import ping


class InternetMonitor:
	def __init__(self, endpoints: Dict[str, str]):
		self.endpoints = dict(endpoints)

	def get_current_latency(self, timeout: float = 2.0) -> Dict[str, Optional[float]]:
		"""
		Get current latency for all endpoints.
		Returns a dictionary with endpoint names as keys and latency in milliseconds as values.
		Returns None for timeouts.
		"""
		results: Dict[str, Optional[float]] = {}
		for name, ip in self.endpoints.items():
			try:
				latency = ping(ip, timeout=timeout)
				if latency is not None:
					results[name] = round(latency * 1000, 2)
				else:
					results[name] = None
			except Exception as e:
				print(f"Error pinging {name} ({ip}): {e}")
				results[name] = None
		return results

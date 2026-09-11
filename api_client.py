import requests

class ForgeApiClient:
    """Helper client to handle raw HTTP calls (Abstraction Layer)."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_health_status(self, timeout: float = 30.0):
        """Executes a GET request to the target endpoint."""
        return requests.get(self.base_url, timeout=timeout)
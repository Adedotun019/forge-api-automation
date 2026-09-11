import requests

class ForgeApiClient:
    """Helper client to handle raw HTTP calls (Abstraction Layer)."""

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_health_status(self, timeout: float = 60.0):
        """Executes a GET request to the target endpoint.
        
        Defaults to 60s timeout to handle cloud cold starts (Render)."""
        return requests.get(self.base_url, timeout=timeout)
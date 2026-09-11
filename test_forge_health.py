import pytest
from api_client import ForgeApiClient

TARGET_URL = "https://forge-us37.onrender.com"


@pytest.fixture
def client():
    """Fixture providing an instance of our abstracted API client."""
    return ForgeApiClient(base_url=TARGET_URL)


def test_forge_endpoint_returns_200_ok(client):
    """Verify endpoint responds with HTTP 200 OK (allows up to 60s for Render cold starts)."""
    # --- ARRANGE ---
    expected_status = 200

    # --- ACT ---
    response = client.get_health_status(timeout=60.0)

    # --- ASSERT ---
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, got {response.status_code}"
    )


def test_forge_endpoint_latency(client):
    """Verify warm endpoint response time is under 5.0 seconds."""
    # --- ARRANGE ---
    max_allowed_seconds = 5.0

    # --- ACT ---
    response = client.get_health_status(timeout=10.0)

    # --- ASSERT ---
    elapsed_time = response.elapsed.total_seconds()
    assert elapsed_time < max_allowed_seconds, (
        f"Response too slow: took {elapsed_time:.2f}s"
    )
import pytest
from api_client import ForgeApiClient

# Shared test configuration
TARGET_URL = "https://forge-us37.onrender.com"


@pytest.fixture
def client():
    """Fixture providing an instance of our abstracted API client."""
    return ForgeApiClient(base_url=TARGET_URL)


def test_forge_endpoint_returns_200_ok(client):
    """Verify endpoint responds with HTTP 200 OK."""
    # --- ARRANGE ---
    expected_status = 200

    # --- ACT ---
    response = client.get_health_status()

    # --- ASSERT ---
    assert response.status_code == expected_status, (
        f"Expected {expected_status}, got {response.status_code}"
    )


def test_forge_endpoint_latency(client):
    """Verify endpoint response time is under 2.0 seconds."""
    # --- ARRANGE ---
    max_allowed_seconds = 2.0

    # --- ACT ---
    response = client.get_health_status()

    # --- ASSERT ---
    elapsed_time = response.elapsed.total_seconds()
    assert elapsed_time < max_allowed_seconds, (
        f"Response too slow: took {elapsed_time:.2f}s"
    )
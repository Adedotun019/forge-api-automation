# Forge API Automation Suite

An automated API test framework for `forge-us37.onrender.com` built in Python using `pytest` and `requests`.

## Engineering Highlights
- **Arrange-Act-Assert (AAA) Pattern:** Every test case explicitly segregates test setup, execution, and assertion phases for maximum readability.
- **Client Abstraction Layer (`api_client.py`):** Low-level HTTP requests are decoupled from test scripts, enforcing DRY (Don't Repeat Yourself) architecture.
- **Infrastructure & Cold-Start Resilience:** Test timeouts are engineered to accommodate free-tier hosting cold starts (up to 60s) while strictly benchmarking warm endpoint latency (< 5.0s).

## Repository Structure

```text
forge-api-automation/
├── api_client.py          # Abstracted HTTP client handling requests & default timeouts
├── test_forge_health.py   # Functional status code & latency benchmark test suite
├── requirements.txt       # Project dependency manifest
├── .gitignore             # Workspace exclusion rules
└── README.md              # Framework documentation
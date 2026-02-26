import requests
import config

# ============================================
# HBCE ROVER CONTROL — ROVER CLIENT
# Centralizes HTTP calls and normalizes errors.
# ============================================

class RoverClient:
    def __init__(self, base_url: str | None = None):
        self.base_url = (base_url or config.ROVER_URL).rstrip("/")

    def _url(self, endpoint: str) -> str:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self.base_url}{endpoint}"

    def get_json(self, endpoint: str) -> dict:
        r = requests.get(self._url(endpoint), timeout=config.HTTP_TIMEOUT_S)
        r.raise_for_status()
        return r.json()

    def post_json(self, endpoint: str, payload: dict) -> dict:
        r = requests.post(self._url(endpoint), json=payload, timeout=config.HTTP_TIMEOUT_S)
        r.raise_for_status()
        return r.json()

    # ---- API wrappers ----
    def status(self) -> dict:
        return self.get_json("/status")

    def log(self) -> dict | list:
        return self.get_json("/log")

    def cmd(self, move: str, v: float = 0.2, ms: int = 300) -> dict:
        return self.post_json("/cmd", {"move": move, "v": v, "ms": ms})

    def mode(self, mode: str) -> dict:
        return self.post_json("/mode", {"mode": mode})

    def estop(self, on: bool = True) -> dict:
        return self.post_json("/estop", {"on": on})

    def arm(self, token: str = "lab") -> dict:
        return self.post_json("/arm", {"token": token})

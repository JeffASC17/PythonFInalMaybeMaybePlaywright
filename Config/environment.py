import os
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")


def get_base_url() -> str:
    value = os.getenv("BASE_URL", "").strip()
    if not value:
        raise RuntimeError("BASE_URL must be set in .env or the process environment.")

    parsed = urlsplit(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"BASE_URL must be an absolute HTTP(S) URL: {value!r}")

    return urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path.rstrip("/") + "/", parsed.query, parsed.fragment)
    )


def resolve_url(base_url: str, path: str) -> str:
    return f"{base_url.rstrip('/')}/{path.lstrip('/')}"

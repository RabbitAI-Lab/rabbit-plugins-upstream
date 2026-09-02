"""Entry point: start the FastAPI app via `python -m src.main`."""
import uvicorn

from src.config import get_config


def main() -> None:
    cfg = get_config()
    host = cfg.as_dict().get("api", {}).get("host", "0.0.0.0") if isinstance(cfg.as_dict().get("api"), dict) else "0.0.0.0"
    port = int(cfg.as_dict().get("api", {}).get("port", 8000)) if isinstance(cfg.as_dict().get("api"), dict) else 8000
    uvicorn.run("src.api.app:app", host=host, port=port, reload=False)


if __name__ == "__main__":
    main()

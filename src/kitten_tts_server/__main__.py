from .server import app


def main() -> None:
    # Delay import of uvicorn to avoid mandatory dependency when embedding
    import uvicorn

    # Import config helpers lazily to honor any environment overrides
    from .config import get_host, get_port

    server_host = get_host()
    server_port = get_port()

    uvicorn.run(
        "kitten_tts_server.server:app",
        host=server_host,
        port=server_port,
        log_level="info",
        workers=1,
        reload=True,
    )


if __name__ == "__main__":
    main()

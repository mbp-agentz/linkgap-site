#!/usr/bin/env python3
"""Serve the linkgap landing page locally.

    python3 site/preview.py

Then open http://127.0.0.1:8142 — plain static files, no build step.
Port 8142 is used on purpose: 8000 is the owner's running linkgap app.
"""

from __future__ import annotations

import functools
import http.server
import pathlib
import socketserver

PORT = 8142
ROOT = pathlib.Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    """Static handler that does not cache, so edits show up on reload."""

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt: str, *args) -> None:  # quieter output
        print("  %s" % (fmt % args))


def main() -> None:
    handler = functools.partial(Handler, directory=str(ROOT))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"linkgap landing page: http://127.0.0.1:{PORT}")
        print("Ctrl-C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()

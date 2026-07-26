"""
HTTP server for skill-radar routing.

Provides a simple REST API for framework-agnostic integration.
Requires: pip install skill-radar[serve]  (adds flask or http.server)

Endpoints:
    POST /route     — Route a query, returns JSON results
    GET  /health    — Health check
    GET  /skills    — List registered skills
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Optional

from skill_radar.loader import load_skills


_router = None


class RouteHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler for routing requests."""

    def do_POST(self):
        if self.path == "/route":
            self._handle_route()
        else:
            self._respond(404, {"error": "Not found"})

    def do_GET(self):
        if self.path == "/health":
            self._respond(200, {"status": "ok", "skills": len(_router.skills) if _router else 0})
        elif self.path == "/skills":
            self._handle_list_skills()
        else:
            self._respond(404, {"error": "Not found"})

    def _handle_route(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length)) if length > 0 else {}
        except (json.JSONDecodeError, ValueError):
            self._respond(400, {"error": "Invalid JSON body"})
            return

        query = body.get("query", "")
        if not query:
            self._respond(400, {"error": "Missing 'query' field"})
            return

        context = body.get("context", {})
        results = _router.route(query, context)

        self._respond(200, {
            "query": query,
            "results": [r.to_dict() for r in results if not r.excluded],
            "excluded": [
                {"skill": r.skill_name, "reason": r.exclude_reason}
                for r in results if r.excluded
            ],
        })

    def _handle_list_skills(self):
        skills = [
            {"name": s.name, "keywords": s.keywords[:5], "priority": s.priority}
            for s in _router.skills
        ]
        self._respond(200, {"skills": skills, "count": len(skills)})

    def _respond(self, status: int, data: dict):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def log_message(self, format, *args):
        """Suppress default logging."""
        pass


def start_server(
    skills_dir: str,
    config: Optional[str] = None,
    port: int = 8900,
    host: str = "127.0.0.1",
):
    """Start the HTTP routing server."""
    global _router
    _router = load_skills(skills_dir, config)

    if not _router.skills:
        print(f"WARNING: No skills with routing declarations found in {skills_dir}")

    print(f"Skill Radar server starting...")
    print(f"  Skills loaded: {len(_router.skills)}")
    print(f"  Listening on:  http://{host}:{port}")
    print(f"  Endpoints:")
    print(f"    POST /route   — Route a query")
    print(f"    GET  /health  — Health check")
    print(f"    GET  /skills  — List skills")
    print()

    server = HTTPServer((host, port), RouteHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()

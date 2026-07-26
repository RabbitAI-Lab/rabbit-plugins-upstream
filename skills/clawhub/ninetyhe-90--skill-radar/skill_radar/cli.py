"""
CLI entry point for skill-radar.

Usage:
    skill-radar route "query" --skills-dir ./skills/
    skill-radar init --skills-dir ./skills/
    skill-radar serve --port 8900
"""

import sys
import json
import argparse
from pathlib import Path

from skill_radar.core import ScoringResult
from skill_radar.loader import load_skills, load_router_config


def cmd_route(args):
    """Execute routing for a single query."""
    router = load_skills(args.skills_dir, args.config)

    if not router.skills:
        print("ERROR: No skills with routing declarations found.", file=sys.stderr)
        sys.exit(1)

    context = {}
    if args.context_json:
        try:
            context = json.loads(args.context_json)
        except json.JSONDecodeError:
            print("WARNING: Invalid context JSON, ignoring.", file=sys.stderr)

    if args.interactive:
        print(f"Loaded {len(router.skills)} skills. Interactive mode (type 'quit' to exit).\n")
        while True:
            try:
                query = input("Query > ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if query.lower() in ("quit", "exit", "q"):
                break
            if not query:
                continue
            results = router.route(query, context)
            _print(results, query, args.verbose, args.format)
            print()
    else:
        if not args.query:
            print("ERROR: --query is required (or use --interactive)", file=sys.stderr)
            sys.exit(1)
        results = router.route(args.query, context)
        _print(results, args.query, args.verbose, args.format)


def cmd_init(args):
    """Auto-generate routing.yaml for skills that don't have one."""
    from skill_radar.init_routing import generate_routing_for_skill

    skills_dir = Path(args.skills_dir)
    if not skills_dir.exists():
        print(f"ERROR: Directory not found: {skills_dir}", file=sys.stderr)
        sys.exit(1)

    generated = 0
    skipped = 0
    for skill_path in sorted(skills_dir.iterdir()):
        if not skill_path.is_dir() or skill_path.name.startswith("."):
            continue
        routing_yaml = skill_path / "routing.yaml"
        if routing_yaml.exists() and not args.force:
            skipped += 1
            continue
        success = generate_routing_for_skill(skill_path, overwrite=args.force)
        if success:
            generated += 1
            print(f"  + {skill_path.name}/routing.yaml")
        else:
            print(f"  - {skill_path.name} (no SKILL.md or unable to parse)")

    print(f"\nDone: {generated} generated, {skipped} skipped (already exist).")
    if skipped > 0:
        print(f"Use --force to overwrite existing routing.yaml files.")


def cmd_serve(args):
    """Start HTTP routing service."""
    try:
        from skill_radar.server import start_server
    except ImportError as e:
        print(f"ERROR: HTTP server requires additional dependencies: {e}", file=sys.stderr)
        print("Install with: pip install skill-radar[serve]", file=sys.stderr)
        sys.exit(1)

    start_server(
        skills_dir=args.skills_dir,
        config=args.config,
        port=args.port,
        host=args.host,
    )


def _print(results: list[ScoringResult], query: str, verbose: bool, fmt: str):
    """Format and print routing results."""
    if fmt == "json":
        output = {
            "query": query,
            "results": [r.to_dict() for r in results if not r.excluded],
            "excluded": [
                {"skill": r.skill_name, "reason": r.exclude_reason}
                for r in results if r.excluded
            ],
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    recalled = [r for r in results if not r.excluded and r.total_score > 0]
    if not recalled:
        print(f"  No match (query: {query})")
        return

    print(f"  Query: \"{query}\"")
    for i, r in enumerate(recalled, 1):
        marker = ">>>" if i == 1 else "   "
        print(f"  {marker} #{i} [{r.skill_name}] score={r.total_score:.4f}")
        if verbose:
            print(f"       kw={r.keyword_score:.3f} pat={r.pattern_score:.3f} "
                  f"int={r.intent_score:.3f} ctx={r.context_score:.3f} "
                  f"pri={r.priority_score:.3f}")
            if r.matched_keywords:
                print(f"       keywords: {r.matched_keywords}")
            if r.matched_patterns:
                print(f"       patterns: {r.matched_patterns}")


def main():
    parser = argparse.ArgumentParser(
        prog="skill-radar",
        description="Skill Radar - Declarative routing engine for multi-skill AI agents",
    )
    subparsers = parser.add_subparsers(dest="command")

    # route subcommand
    p_route = subparsers.add_parser("route", help="Route a query to matching skills")
    p_route.add_argument("query", nargs="?", help="Query text")
    p_route.add_argument("--skills-dir", "-s", required=True, help="Skills directory path")
    p_route.add_argument("--config", "-c", help="Router config file path")
    p_route.add_argument("--context-json", help="Context JSON string")
    p_route.add_argument("--interactive", "-i", action="store_true", help="Interactive mode")
    p_route.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    p_route.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    p_route.set_defaults(func=cmd_route)

    # init subcommand
    p_init = subparsers.add_parser("init", help="Auto-generate routing.yaml for skills")
    p_init.add_argument("--skills-dir", "-s", required=True, help="Skills directory path")
    p_init.add_argument("--force", "-f", action="store_true", help="Overwrite existing routing.yaml")
    p_init.set_defaults(func=cmd_init)

    # serve subcommand
    p_serve = subparsers.add_parser("serve", help="Start HTTP routing service")
    p_serve.add_argument("--skills-dir", "-s", required=True, help="Skills directory path")
    p_serve.add_argument("--config", "-c", help="Router config file path")
    p_serve.add_argument("--port", "-p", type=int, default=8900, help="Server port")
    p_serve.add_argument("--host", default="127.0.0.1", help="Server host")
    p_serve.set_defaults(func=cmd_serve)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    args.func(args)


if __name__ == "__main__":
    main()

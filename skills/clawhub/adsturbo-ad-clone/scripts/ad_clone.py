#!/usr/bin/env python3
"""Ad cloning: study a reference video, then shoot your own version of it.

analyze  : break a reference down into a prompt + shot list (clips capped at 12s)
generate : produce a new video from that prompt
inspect  : plain shot-by-shot analysis of any video, no generation
"""

from __future__ import annotations

import argparse

from shared.client import add_async_flags, run_cli, submit_and_maybe_poll

ANALYZE = "/openapi/v1/adclone/analyze"
GENERATE = "/openapi/v1/adclone/generate"
INSPECT = "/openapi/v1/video/analyze"


def cmd_analyze(client, args) -> dict:
    """Synchronous -- returns the prompt to feed into `generate`."""
    return client.post(ANALYZE, {
        "video_url": args.video_url,
        "clip_start": args.clip_start,
        "clip_end": args.clip_end,
    })


def cmd_generate(client, args) -> dict:
    return submit_and_maybe_poll(client, GENERATE, {
        "prompt": args.prompt,
        "video_url": args.video_url,
        "duration": args.duration,
        "ratio": args.ratio,
        "callback_id": args.callback_id,
        "idempotency_key": args.idempotency_key,
    }, args)


def cmd_inspect(client, args) -> dict:
    return submit_and_maybe_poll(client, INSPECT, {
        "video_url": args.video_url,
        "workspace_id": args.workspace_id,
        "callback_id": args.callback_id,
        "idempotency_key": args.idempotency_key,
    }, args)


def cmd_query(client, args) -> dict:
    return client.poll(args.workspace_id, timeout=args.timeout, interval=args.interval)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AdsTurbo ad cloning")
    sub = parser.add_subparsers(dest="command")

    ana = sub.add_parser("analyze", help="turn a reference video into a prompt")
    ana.add_argument("--video-url", required=True)
    ana.add_argument("--clip-start", type=int, help="seconds; trim before analysing")
    ana.add_argument("--clip-end", type=int)

    gen = sub.add_parser("generate", help="shoot a new video from an analysed prompt")
    gen.add_argument("--prompt", required=True, help="usually the output of `analyze`")
    gen.add_argument("--video-url", default="", help="the reference, for style anchoring")
    gen.add_argument("--duration", type=int)
    gen.add_argument("--ratio", default="")
    gen.add_argument("--idempotency-key", default="")
    add_async_flags(gen)

    ins = sub.add_parser("inspect", help="shot-by-shot analysis, no generation")
    ins.add_argument("--video-url", default="")
    ins.add_argument("--workspace-id", default="")
    ins.add_argument("--idempotency-key", default="")
    add_async_flags(ins)

    query = sub.add_parser("query", help="resume polling a known workspace_id")
    query.add_argument("--workspace-id", required=True)
    query.add_argument("--timeout", type=float, default=900)
    query.add_argument("--interval", type=float, default=10)

    return parser


HANDLERS = {
    "analyze": cmd_analyze,
    "generate": cmd_generate,
    "inspect": cmd_inspect,
    "query": cmd_query,
}

if __name__ == "__main__":
    run_cli(build_parser(), HANDLERS)

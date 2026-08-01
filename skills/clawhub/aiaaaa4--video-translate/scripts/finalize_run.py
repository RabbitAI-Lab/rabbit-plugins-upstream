#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from video_to_subtitles import (
    DEFAULT_GLOSSARY,
    DEFAULT_TERM_RULES,
    bind_output_naming,
    default_subtitle_tag,
    default_outputs_dir,
    export_subtitle_files,
    final_qc_gate,
    model_name_from_env,
    record_step_timing,
    record_step_status,
    resolve_localized_output_title,
    run_deterministic_qa,
    semantic_review_gate,
    source_analysis_gate,
    validate_subtitle_tag,
    write_run_summary,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Finalize an existing run without rerunning ASR or regenerating the AI prompt.")
    parser.add_argument("run_dir", type=Path, help="Existing run directory that contains work/segments.txt and work/word_table.json.")
    parser.add_argument("--media", type=Path, default=None, help="Original media path, used for localized output naming and the final chat summary.")
    parser.add_argument("--localized-title", default=None, help="Clean Chinese title without a date, platform ID, extension, or subtitle tag.")
    parser.add_argument("--subtitle-tag", default=None, help="Localized subtitle suffix; defaults from --language.")
    parser.add_argument(
        "--output-base",
        default=None,
        help="Legacy explicit output basename. It must still contain a clean Chinese title and the localized subtitle tag.",
    )
    parser.add_argument("--outputs-dir", type=Path, default=None)
    parser.add_argument("--language", default="en")
    parser.add_argument("--domain-name", default="finance/trading training videos")
    parser.add_argument("--glossary", type=Path, default=DEFAULT_GLOSSARY)
    parser.add_argument("--term-rules", type=Path, default=DEFAULT_TERM_RULES)
    parser.add_argument("--disable-domain-term-checks", action="store_true")
    parser.add_argument("--source-first", action="store_true")
    parser.add_argument("--orchestrator-model", default=None, help="Name of the AI model orchestrating this run, for the final chat summary.")
    parser.add_argument("--translation-model", default=None, help="Optional model label used only in the final run summary.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    started_at = time.monotonic()
    run_dir = args.run_dir.expanduser().resolve()
    work_dir = run_dir / "work"
    subtitles_dir = run_dir / "subtitles"
    outputs_dir = args.outputs_dir or default_outputs_dir()
    if not outputs_dir.is_absolute():
        outputs_dir = Path.cwd() / outputs_dir

    if not (work_dir / "segments.txt").exists():
        raise FileNotFoundError(f"Missing {work_dir / 'segments.txt'}")
    if not (work_dir / "word_table.json").exists():
        raise FileNotFoundError(f"Missing {work_dir / 'word_table.json'}")

    media = args.media.expanduser().resolve() if args.media else Path("unknown")
    output_tag = validate_subtitle_tag(args.subtitle_tag or default_subtitle_tag(args.language))
    naming_path = work_dir / "output_naming.json"
    if naming_path.exists():
        naming = json.loads(naming_path.read_text(encoding="utf-8"))
        output_base = str(naming.get("output_base") or "")
        if not output_base:
            raise RuntimeError(f"Invalid output naming record: {naming_path}")
        if args.media and str(media) != naming.get("media"):
            raise RuntimeError("This run is already bound to a different media path.")
        if args.output_base and args.output_base != output_base:
            raise RuntimeError("This run is already bound to different output naming.")
        if args.localized_title and args.localized_title != naming.get("localized_title"):
            raise RuntimeError("This run is already bound to different output naming.")
        if args.subtitle_tag and args.subtitle_tag != naming.get("output_tag"):
            raise RuntimeError("This run is already bound to a different subtitle tag.")
        localized_title = str(naming.get("localized_title") or "")
        title_source = str(naming.get("title_source") or "")
        bound_output_tag = validate_subtitle_tag(str(naming.get("output_tag") or ""))
        bound_media = Path(str(naming.get("media") or ""))
        verified_title, _ = resolve_localized_output_title(bound_media, localized_title)
        if verified_title != localized_title or output_base != f"{localized_title}.{bound_output_tag}":
            raise RuntimeError(f"Invalid output naming record: {naming_path}")
        if not args.media:
            media = bound_media
        bind_output_naming(
            work_dir,
            bound_media,
            localized_title,
            title_source,
            bound_output_tag,
            output_base,
        )
    else:
        if args.output_base:
            suffix = f".{output_tag}"
            if not args.output_base.endswith(suffix):
                raise RuntimeError(f"--output-base must end with {suffix}")
            requested_title = args.output_base[: -len(suffix)]
            localized_title, title_source = resolve_localized_output_title(media, requested_title)
        else:
            if not args.media:
                raise RuntimeError(
                    "Re-export requires --media or an existing output_naming.json so the clean Chinese title can be verified."
                )
            localized_title, title_source = resolve_localized_output_title(media, args.localized_title)
        output_base = f"{localized_title}.{output_tag}"
        bind_output_naming(work_dir, media, localized_title, title_source, output_tag, output_base)

    step_started = time.monotonic()
    source_subtitle = None
    meta_path = work_dir / "segment_generation_meta.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        candidate = Path(str(meta.get("source_subtitle") or ""))
        source_subtitle = candidate if str(candidate) and candidate.is_file() else None
    config_path = work_dir / "workflow_config.json"
    workflow_config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    translation_provider = str(workflow_config.get("translation_provider") or "qwen-mt-plus")
    record_step_status(work_dir, "source_analysis", "running", "finalize existing run")
    if not source_analysis_gate(run_dir / "transcript", work_dir, source_subtitle, translation_provider):
        record_step_status(work_dir, "source_analysis", "waiting", "complete source-analysis receipt")
        return 3
    record_step_status(work_dir, "source_analysis", "done")
    record_step_status(work_dir, "semantic_review", "running", "finalize existing run")
    if not semantic_review_gate(work_dir):
        record_step_status(work_dir, "semantic_review", "waiting", "complete semantic-review receipt")
        return 5
    record_step_status(work_dir, "semantic_review", "done")
    record_step_status(work_dir, "deterministic_qa", "running", "finalize existing run")
    run_deterministic_qa(
        work_dir,
        args.domain_name,
        args.glossary,
        args.term_rules,
        args.disable_domain_term_checks,
    )
    record_step_status(work_dir, "deterministic_qa", "done")
    record_step_status(work_dir, "global_qc", "running", "finalize existing run")
    if not final_qc_gate(work_dir):
        record_step_status(work_dir, "global_qc", "waiting", "complete final-QC receipt")
        return 6
    record_step_status(work_dir, "global_qc", "done")
    export_subtitle_files(work_dir, subtitles_dir, outputs_dir, output_base, args.source_first)
    record_step_timing(work_dir, "export", time.monotonic() - step_started, "finalize existing run")
    elapsed = time.monotonic() - started_at
    orchestrator_model = model_name_from_env(args.orchestrator_model)
    translation_model = args.translation_model or ("current Agent model" if translation_provider == "agent" else "qwen-mt-plus")
    write_run_summary(work_dir, run_dir, media, args.language, args.domain_name, outputs_dir, output_base, elapsed, orchestrator_model, translation_model)
    print(f"Done in {elapsed:.1f}s ({elapsed / 60:.1f} min)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

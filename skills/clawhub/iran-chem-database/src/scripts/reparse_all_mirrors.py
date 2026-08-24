"""Re-parse all existing mirrors WITHOUT re-downloading (remediation §5).

Usage:
  python -m src.scripts.reparse_all_mirrors [--inclusion-mode MODE] [--supplier ID]

Modes: research_only | lab_or_research | all_identifiable_catalogue
(default: the configured parsing.inclusion_mode).

Reports mirrors discovered, candidates, accepted records, per-reason
rejection counts and sync errors; preserves provenance and updates
timestamps; exits nonzero when the failure fraction exceeds
parsing.reparse_failure_threshold (default 5%).
"""
from __future__ import annotations

import argparse
import sys

from sqlalchemy import delete, select

from src.config import get_config
from src.crawler.httrack_config import HTTrackMirrorConfig
from src.crawler.httrack_engine import HTTrackMirrorEngine
from src.database.live_sync import LiveSyncEngine
from src.database.models import RejectedCatalogueItem, Supplier
from src.database.session import get_db_session
from src.parser.product_extractor import MoleculeExtractorPipeline


def main() -> int:
    parser = argparse.ArgumentParser(description="Re-parse all local HTTrack mirrors.")
    parser.add_argument("--inclusion-mode", default=None,
                        choices=["research_only", "lab_or_research", "all_identifiable_catalogue",
                                 "strict_research", "all_catalogue"],
                        help="Override the configured parsing.inclusion_mode")
    parser.add_argument("--supplier", type=int, default=None, help="Reparse a single supplier ID")
    args = parser.parse_args()

    cfg = get_config()
    parsing = cfg.as_dict().get("parsing", {}) or {}
    mode = args.inclusion_mode or parsing.get("inclusion_mode", "all_identifiable_catalogue")
    threshold = float(parsing.get("reparse_failure_threshold", 0.05))

    db = get_db_session()
    engine = HTTrackMirrorEngine()
    total_files = 0
    total_candidates = 0
    total_accepted = 0
    total_rejected_grade = 0
    total_rejected_validation = 0
    total_rejected_sync = 0
    total_errors = 0
    suppliers_done = 0

    try:
        q = select(Supplier)
        if args.supplier is not None:
            q = q.where(Supplier.supplier_id == args.supplier)
        suppliers = db.execute(q).scalars().all()

        for supplier in suppliers:
            if not supplier.httrack_mirror_path:
                print(f"skip {supplier.company_name_en}: no mirror path")
                continue
            config = HTTrackMirrorConfig(
                supplier_id=supplier.supplier_id,
                project_name=supplier.httrack_project_name or f"supplier_{supplier.supplier_id}",
                urls=[supplier.website_url],
                output_dir=supplier.httrack_mirror_path,
            )
            files = engine.get_all_parseable_files(config)
            if not files:
                print(f"skip {supplier.company_name_en}: no mirror files")
                continue

            # stale audit rows are replaced by the CURRENT policy's view
            db.execute(delete(RejectedCatalogueItem).where(
                RejectedCatalogueItem.supplier_id == supplier.supplier_id))
            db.commit()

            sync = LiveSyncEngine(db)
            extractor = MoleculeExtractorPipeline(db_sync=sync, inclusion_mode=mode,
                                                  supplier_is_lab=True)
            results = extractor.process_files(files, supplier.supplier_id, config.output_dir)
            sync.commit()

            total_files += len(files)
            total_candidates += results["total_found"] + results["rejected_grade"] + results["rejected_validation"]
            total_accepted += results["total_found"]
            total_rejected_grade += results["rejected_grade"]
            total_rejected_validation += results["rejected_validation"]
            total_rejected_sync += results["rejected_sync"]
            total_errors += len(results["errors"])
            suppliers_done += 1
            print(f"{supplier.company_name_en}: {len(files)} files, "
                  f"accepted={results['total_found']} (new={results['new_count']}, upd={results['updated_count']}), "
                  f"rejected_grade={results['rejected_grade']}, "
                  f"rejected_validation={results['rejected_validation']}, "
                  f"sync_errors={results['rejected_sync']}, parse_errors={len(results['errors'])}")

        print(f"Done. {suppliers_done} suppliers, {total_files} mirror files, "
              f"{total_candidates} candidates, {total_accepted} accepted "
              f"(grade_rejected={total_rejected_grade}, validation_rejected={total_rejected_validation}, "
              f"sync_rejected={total_rejected_sync}), errors={total_errors}")

        failure_frac = (total_errors + total_rejected_sync) / max(total_candidates, 1)
        if failure_frac > threshold:
            print(f"FAILED: failure fraction {failure_frac:.3f} exceeds threshold {threshold}", file=sys.stderr)
            return 1
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    sys.exit(main())

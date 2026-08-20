"""Re-parse all existing mirrors WITHOUT re-downloading (spec §9)."""
from __future__ import annotations

import sys

from sqlalchemy import select

from src.crawler.httrack_engine import HTTrackMirrorEngine
from src.crawler.httrack_config import HTTrackMirrorConfig
from src.database.live_sync import LiveSyncEngine
from src.database.models import Supplier
from src.database.session import get_db_session
from src.parser.product_extractor import MoleculeExtractorPipeline


def main() -> None:
    db = get_db_session()
    engine = HTTrackMirrorEngine()
    try:
        suppliers = db.execute(select(Supplier)).scalars().all()
        total = 0
        for supplier in suppliers:
            if not supplier.httrack_mirror_path:
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
            sync = LiveSyncEngine(db)
            extractor = MoleculeExtractorPipeline(db_sync=sync)
            results = extractor.process_files(files, supplier.supplier_id, config.output_dir)
            sync.commit()
            total += results["total_found"]
            print(f"{supplier.company_name_en}: {len(files)} files -> {results['total_found']} molecules")
        print(f"Done. {total} molecules re-parsed.")
    finally:
        db.close()


if __name__ == "__main__":
    main()

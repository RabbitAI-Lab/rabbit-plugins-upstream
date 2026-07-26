# Batch processing module
# Scans a directory for video files and runs the full analysis workflow on each,
# storing a batch summary in Supabase and publishing reports grouped by category.
import os
import time
import traceback
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional

# Common video container extensions
VIDEO_EXTENSIONS = {
    ".mp4", ".mov", ".mkv", ".avi", ".webm", ".flv", ".wmv", ".m4v", ".mpeg", ".mpg", ".ts",
}


@dataclass
class ItemResult:
    video_path: str
    category: str
    status: str  # "completed" | "failed"
    video_id: Optional[str] = None
    feishu_wiki_url: Optional[str] = None
    frames_processed: int = 0
    error: Optional[str] = None


@dataclass
class BatchResult:
    batch_id: Optional[str]
    directory: str
    total: int
    succeeded: int
    failed: int
    items: List[ItemResult] = field(default_factory=list)


def discover_videos(directory: str, recursive: bool = True) -> List[str]:
    """Return sorted list of video files under `directory`."""
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Not a directory: {directory}")

    found: List[str] = []
    if recursive:
        for root, _dirs, files in os.walk(directory):
            for name in files:
                if os.path.splitext(name)[1].lower() in VIDEO_EXTENSIONS:
                    found.append(os.path.join(root, name))
    else:
        for name in os.listdir(directory):
            full = os.path.join(directory, name)
            if os.path.isfile(full) and os.path.splitext(name)[1].lower() in VIDEO_EXTENSIONS:
                found.append(full)
    return sorted(found)


def classify_video(video_path: str, base_dir: str, rules: Optional[Dict[str, str]] = None) -> str:
    """
    Derive a category for a video.

    Priority:
      1. Explicit keyword rules (substring match against the relative path, case-insensitive).
      2. First sub-directory under base_dir (folder-based categorization).
      3. "uncategorized".
    """
    rel = os.path.relpath(video_path, base_dir)
    rel_lower = rel.lower()

    if rules:
        for keyword, category in rules.items():
            if keyword.lower() in rel_lower:
                return category

    parts = rel.split(os.sep)
    if len(parts) > 1 and parts[0]:
        return parts[0]

    return "uncategorized"


class BatchProcessor:
    """
    Orchestrates batch video processing on top of an existing VideoAnalyzer.

    The analyzer is injected so this module stays decoupled from main.py and is
    easy to unit-test with a fake analyzer.
    """

    def __init__(self, analyzer, db_client=None, wiki_client=None):
        self.analyzer = analyzer
        # Reuse analyzer's clients when not explicitly provided.
        self.db_client = db_client or getattr(analyzer, "db_client", None)
        self.wiki_client = wiki_client or getattr(analyzer, "wiki_client", None)

    def process_directory(
        self,
        directory: str,
        user_id: str,
        space_id: str,
        recursive: bool = True,
        category_rules: Optional[Dict[str, str]] = None,
        continue_on_error: bool = True,
        progress: Optional[Callable[[str], None]] = None,
    ) -> BatchResult:
        log = progress or print
        directory = os.path.abspath(directory)

        videos = discover_videos(directory, recursive=recursive)
        log(f"Discovered {len(videos)} video(s) under {directory}")

        batch_id = None
        if self.db_client and hasattr(self.db_client, "save_batch_run"):
            try:
                batch_id = self.db_client.save_batch_run(
                    user_id=user_id, directory=directory, total=len(videos)
                )
            except Exception as e:  # noqa: BLE001 - batch tracking is best-effort
                log(f"WARN: failed to create batch run record: {e}")

        # Cache of category -> parent node token so pages with the same category
        # are grouped under one Wiki node and we avoid recreating it per video.
        category_nodes: Dict[str, Optional[str]] = {}
        items: List[ItemResult] = []

        for idx, video_path in enumerate(videos, 1):
            category = classify_video(video_path, directory, category_rules)
            log(f"[{idx}/{len(videos)}] {os.path.basename(video_path)} -> category '{category}'")

            parent_token = self._ensure_category_parent(space_id, category, category_nodes, log)

            try:
                result = self.analyzer.process_video(
                    video_path=video_path,
                    user_id=user_id,
                    space_id=space_id,
                    parent_node_token=parent_token,
                    category=category,
                )
                items.append(
                    ItemResult(
                        video_path=video_path,
                        category=category,
                        status="completed",
                        video_id=result.get("video_id"),
                        feishu_wiki_url=result.get("feishu_wiki_url"),
                        frames_processed=result.get("frames_processed", 0),
                    )
                )
            except Exception as e:  # noqa: BLE001 - isolate per-video failures
                err = f"{type(e).__name__}: {e}"
                log(f"ERROR processing {video_path}: {err}")
                log(traceback.format_exc())
                items.append(
                    ItemResult(
                        video_path=video_path, category=category, status="failed", error=err
                    )
                )
                if not continue_on_error:
                    break

        succeeded = sum(1 for i in items if i.status == "completed")
        failed = sum(1 for i in items if i.status == "failed")

        if batch_id and self.db_client and hasattr(self.db_client, "update_batch_run"):
            try:
                self.db_client.update_batch_run(
                    batch_id,
                    status="completed" if failed == 0 else "completed_with_errors",
                    succeeded=succeeded,
                    failed=failed,
                )
            except Exception as e:  # noqa: BLE001
                log(f"WARN: failed to finalize batch run record: {e}")

        return BatchResult(
            batch_id=batch_id,
            directory=directory,
            total=len(videos),
            succeeded=succeeded,
            failed=failed,
            items=items,
        )

    def _ensure_category_parent(
        self,
        space_id: str,
        category: str,
        cache: Dict[str, Optional[str]],
        log: Callable[[str], None],
    ) -> Optional[str]:
        if category in cache:
            return cache[category]

        token = None
        if self.wiki_client and hasattr(self.wiki_client, "ensure_category_node"):
            try:
                token = self.wiki_client.ensure_category_node(space_id, category)
            except Exception as e:  # noqa: BLE001 - fall back to space root on failure
                log(f"WARN: could not ensure category node '{category}': {e}")
                token = None
        cache[category] = token
        return token

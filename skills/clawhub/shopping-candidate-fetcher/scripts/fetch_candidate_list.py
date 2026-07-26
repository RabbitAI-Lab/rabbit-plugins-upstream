import argparse
import json
from pathlib import Path
from typing import Any, Dict

BASE_DIR = Path(__file__).resolve().parent.parent
QUERY_INDEX_PATH = BASE_DIR / "data" / "query_index.json"
SNAPSHOT_DIR = BASE_DIR / "data" / "snapshots"


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_query_index() -> Dict[str, str]:
    return load_json(QUERY_INDEX_PATH)


def normalize_candidate(candidate: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "rank": candidate.get("rank"),
        "item_id": candidate.get("item_id") or candidate.get("candidate_id"),
        "title": candidate.get("title") or candidate.get("product_name") or candidate.get("name"),
        "brand": candidate.get("brand") or candidate.get("brand_name"),
        "price": candidate.get("price"),
        "sales_text": candidate.get("sales_text"),
        "rating": candidate.get("rating"),
        "shop": candidate.get("shop"),
        "location": candidate.get("location"),
        "description": candidate.get("description"),
        "url": candidate.get("url"),
        "is_ad": bool(candidate.get("is_ad", False)),
    }


def fetch_candidate_list(query: str, top_k: int = 5) -> Dict[str, Any]:
    if not query or not query.strip():
        raise ValueError("query must be a non-empty string")
    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    query_index = load_query_index()
    if query not in query_index:
        raise ValueError(
            f"No clean snapshot found for query: {query}. "
            "Please add this query to data/query_index.json first."
        )

    snapshot = load_json(SNAPSHOT_DIR / query_index[query])
    raw_candidates = snapshot.get("candidate_list") or snapshot.get("candidates") or []
    candidates = [normalize_candidate(item) for item in raw_candidates[:top_k]]

    return {
        "skill_name": "shopping-candidate-fetcher",
        "skill_version": "base_v0.2-screenshot-snapshot",
        "source": "shopping_platform_screenshot_snapshot",
        "query_id": snapshot.get("query_id"),
        "query": snapshot.get("query") or snapshot.get("user_query") or query,
        "search_keyword": snapshot.get("search_keyword"),
        "source_platform": snapshot.get("source_platform"),
        "capture_method": snapshot.get("capture_method", "screenshot"),
        "screenshot_file": snapshot.get("screenshot_file"),
        "capture_date": snapshot.get("capture_date"),
        "top_k": top_k,
        "candidates": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch shopping candidates from local snapshots.")
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    print(json.dumps(fetch_candidate_list(args.query, args.top_k), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

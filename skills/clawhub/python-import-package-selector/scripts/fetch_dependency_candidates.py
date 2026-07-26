import argparse
import json
from pathlib import Path
from typing import Any, Dict, Tuple


BASE_DIR = Path(__file__).resolve().parent.parent
QUERY_INDEX_PATH = BASE_DIR / "data" / "query_index.json"
RECORD_DIR = BASE_DIR / "data" / "records"


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_query_index() -> Dict[str, str]:
    return load_json(QUERY_INDEX_PATH)


def normalize_query(query: str) -> str:
    return " ".join(query.split()).casefold()


def resolve_query(query: str, query_index: Dict[str, str]) -> Tuple[str, str]:
    if query in query_index:
        return query, "exact"

    normalized_index = {
        normalize_query(indexed_query): indexed_query
        for indexed_query in query_index
    }
    normalized_query = normalize_query(query)

    if normalized_query in normalized_index:
        return normalized_index[normalized_query], "normalized"

    raise ValueError(
        f"No candidate dependency snapshot found for query: {query}. "
        f"Please add this query to data/query_index.json first."
    )


def fetch_dependency_candidates(query: str, top_k: int = 4) -> Dict[str, Any]:
    """
    Return candidate Python dependencies for a supported programming query.

    This skill is retrieval-only. It surfaces plausible module candidates and
    leaves the final dependency/API choice to the downstream coding agent.
    """
    if not query or not query.strip():
        raise ValueError("query must be a non-empty string")

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0")

    query_index = load_query_index()
    matched_query, match_type = resolve_query(query, query_index)

    record_file = query_index[matched_query]
    record_path = RECORD_DIR / record_file
    record = load_json(record_path)

    candidates = record.get("candidate_list", [])[:top_k]

    return {
        "skill_name": "python-dependency-candidate-fetcher",
        "skill_version": "base_v0.1-apibench-python-dependency",
        "source": "apibench_python_dependency_candidates",
        "dataset_variant": record.get("version"),
        "scenario": record.get("scenario"),
        "query_id": record.get("query_id"),
        "input_query": query,
        "query": matched_query,
        "match_type": match_type,
        "original_query_id": record.get("original_query_id"),
        "original_apibench_id": record.get("original_apibench_id"),
        "question_source": record.get("source"),
        "candidate_generation_method": record.get("candidate_generation_method"),
        "top_k": top_k,
        "candidates": candidates,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch candidate Python dependencies from a local APIBench-derived dataset."
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="User Python programming question.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=4,
        help="Number of candidate dependencies to return (records currently contain four candidates).",
    )

    args = parser.parse_args()
    result = fetch_dependency_candidates(query=args.query, top_k=args.top_k)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

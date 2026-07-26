from scripts.fetch_dependency_candidates import fetch_dependency_candidates


def fetch_candidates(record):
    result = fetch_dependency_candidates(
        query=record["user_query"],
        top_k=len(record["candidate_dependencies"])
    )

    visible = []
    for c in result["candidates"]:
        visible.append({
            "name": c.get("dependency_name") or c.get("name"),
            "description": c.get("description", "")
        })

    return visible
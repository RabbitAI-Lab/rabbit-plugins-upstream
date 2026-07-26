"""
Example usage of search-intelligence-skill.
Demonstrates all major features with real-world scenarios.
"""

from search_intelligence_skill import SearchSkill, Depth


def main():
    # Initialize with your SearXNG instance
    skill = SearchSkill(
        searxng_url="http://localhost:8888",
        timeout=30.0,
        auto_refine=True,
    )

    # Check SearXNG is running
    if not skill.health_check():
        print("⚠ SearXNG instance not reachable!")
        return

    print("=" * 70)
    print("EXAMPLE 1: Site Audit — Check your own site's public exposure")
    print("=" * 70)
    report = skill.search(
        "check publicly indexed pages on my-own-domain.com for a security self-audit",
        depth="deep",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 2: Company Research — Find public info about a business")
    print("=" * 70)
    report = skill.search(
        "public company information and press coverage for example-corp.com",
        depth="deep",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 3: Academic — Research papers on transformers")
    print("=" * 70)
    report = skill.search(
        "latest research papers on transformer architecture 2024",
        depth="standard",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 4: SEO — Analyze a competitor site")
    print("=" * 70)
    report = skill.search(
        "SEO analysis of competitor.com — indexation, backlinks, technical issues",
        depth="deep",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 5: Direct dork query")
    print("=" * 70)
    report = skill.search_dork(
        'site:github.com "changelog" filetype:md',
        engines=["google", "bing"],
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 6: Preview queries without executing")
    print("=" * 70)
    dorks = skill.suggest_queries(
        "find public API documentation on target.com"
    )
    for d in dorks:
        print(f"  [{', '.join(d.operators_used)}] {d.query}")
        print(f"    Purpose: {d.purpose}")
    print()

    print("=" * 70)
    print("EXAMPLE 7: Build a custom dork")
    print("=" * 70)
    dork = skill.build_dork(
        keyword="confidential",
        domain="example.com",
        filetype="pdf",
        intitle="report",
        exclude=["public", "template"],
        exact_match=True,
    )
    print(f"  Generated: {dork.query}")
    # Then execute it:
    # report = skill.search_dork(dork.query)
    print()

    print("=" * 70)
    print("EXAMPLE 8: Code search — find Python libraries")
    print("=" * 70)
    report = skill.search(
        "python library for PDF text extraction with OCR support",
        depth="standard",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 9: News — recent events")
    print("=" * 70)
    report = skill.search(
        "latest news on AI regulation this week",
        depth="standard",
    )
    print(report.to_context())
    print()

    print("=" * 70)
    print("EXAMPLE 10: Deep research chain — multi-source topic report")
    print("=" * 70)
    report = skill.execute_strategy(
        strategy_name="deep_research",
        target="renewable energy trends 2026",
        depth="exhaustive",
    )
    print(report.to_context())
    print()

    # Access structured data programmatically
    print("=" * 70)
    print("PROGRAMMATIC ACCESS")
    print("=" * 70)
    report = skill.search("python async frameworks comparison", depth="quick")
    print(f"Top {len(report.top(3))} results:")
    for r in report.top(3):
        print(f"  [{r.relevance:.1f}] {r.title}")
        print(f"       {r.url}")
    print(f"\nSuggestions: {report.suggestions}")
    print(f"Engines used: {report.engines_used}")
    print(f"Intent: {report.intent.category.value}/{report.intent.subcategory}")

    skill.close()


if __name__ == "__main__":
    main()
---
name: dataify-router
description: Route broad web research, search, scraping, monitoring, media, marketplace, social, travel, jobs, maps, or competitive-intelligence requests to the smallest suitable Dataify skill set. Use when the user describes an outcome rather than naming a specific Dataify API or scraper.
---

# Dataify Router

Translate the user's outcome into a capability plan, then invoke the minimum required skills.

## Workflow

1. Restate the desired deliverable, target sources, scope, freshness, and output format.
2. Select capabilities from `references/capability-map.md`.
3. Prefer a synchronous SERP or Web Unlocker call for discovery. Use Builder scrapers when structured platform data is required.
4. Ask only for missing required inputs. Do not ask for fields that have safe documented defaults.
5. Confirm before high-volume, media-download, or asynchronous Builder jobs. A clear request such as “直接执行” counts as confirmation when scope and cost drivers are already visible.
6. Never expose an API token in commands or output. Read `DATAIFY_API_TOKEN` from the environment.
7. For Builder jobs, hand the returned task ID to `dataify-task-operations`; do not treat task creation as the user's final outcome unless they explicitly requested only submission.
8. Return a concise answer by default. Provide raw output when the user asks for it.

## Routing Rules

- Use a `serp-*` skill for search-engine discovery and fresh result pages.
- Use `dataify-web-unlocker` for a known page requiring rendering or access handling.
- Use a `scraper-*` skill for structured platform records.
- Combine discovery and structured scraping only when discovery is needed to identify target URLs or IDs.
- If several platforms are requested, state the source plan and run independent sources separately.

## Output

Return the result, source coverage, important limitations, and any remaining asynchronous task state. Do not dump large raw payloads into chat unless requested.


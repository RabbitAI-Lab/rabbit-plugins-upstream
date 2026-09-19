## Description:

Compare restaurant menu breadth, matched dishes, bundles, and location-specific prices with the Crawlora API for restaurant competitor benchmarks or comparisons of direct, pickup, and delivery menus in a defined market.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and restaurant operators use this skill to collect comparable restaurant menu data for defined branches, dishes, and order modes. It supports benchmark tables, coverage summaries, and cautious price-positioning hypotheses based on returned menu evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a third-party Crawlora API key and sends requests to Crawlora API endpoints.

Mitigation: Keep CRAWLORA_API_KEY in the environment, avoid logging it, and install the skill only when use of Crawlora as a third-party API provider is acceptable.

Risk: Menu comparisons can be misleading when location precision, order mode, branch identity, collection time, or request volume are outside the intended benchmark scope.

Mitigation: Use the minimum location precision and request volume needed, compare matched branches and modes, preserve collection timestamps, and report missing or partial fetches as coverage limits.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/crawlora-org/skills/restaurant-menu-benchmarking)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown table with concise benchmark narrative and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source IDs, API request paths, collection times, match confidence, coverage notes, and missing-source summaries when available.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

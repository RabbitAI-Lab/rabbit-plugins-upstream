## Description:

Compare restaurant menu breadth, matched dishes, bundles, and location-specific prices with the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to collect scoped restaurant menu data through Crawlora, compare branches and order modes, and produce matched price and coverage benchmarks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scoped restaurant, location, and menu queries are sent to Crawlora with the user's API key.

Mitigation: Use a limited API key where possible, keep it out of shared logs or screenshots, and keep collection within the intended benchmark scope.

Risk: Partial fetches, missing prices, or mismatched branches can lead to misleading menu comparisons.

Mitigation: Check application codes as well as HTTP status, preserve null prices and availability flags, verify branch addresses, and report missing sources instead of treating them as empty menus.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/restaurant-menu-benchmarking)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown benchmark report with tables, coverage summaries, source notes, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes branch addresses, source IDs, API request paths, collection times, availability, match confidence, price differences, unmatched items, and missing sources.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

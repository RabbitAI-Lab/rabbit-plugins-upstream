## Description:

Compare restaurant menu breadth, matched dishes, bundles, and location-specific prices with the Crawlora API for competitor benchmarks in a defined market.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and restaurant operators use this skill to collect comparable restaurant menu data, match items across branches and platforms, and produce benchmark tables with coverage notes and price-difference calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends restaurant search terms, coordinates, menu request parameters, and a Crawlora API key to a third-party Crawlora API.

Mitigation: Keep the API key in the environment, review requested locations and branches before running benchmarks, and avoid including sensitive business notes in request bodies unless approved for that service.

Risk: Incomplete or failed API responses can be mistaken for an empty market or menu catalog.

Mitigation: Check application response codes as well as HTTP status, stop on authorization failures, back off on rate limits, retry transient server errors once, and preserve coverage notes for missing sources.

Risk: Menu surfaces differ by source, order mode, and branch, so prices or item availability can be miscompared.

Mitigation: Compare matched branches and order modes, preserve source-specific price fields and availability flags, and report positioning or menu gaps as hypotheses rather than proof of demand, margin, or sales volume.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/restaurant-menu-benchmarking)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with tables and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Benchmark output should include collection time, source, branch or address, order mode, item matching details, availability, confidence, price differences, and coverage notes.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

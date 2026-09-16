## Description:

Queries Crawlora's pre-built hosted datasets through search, facets, item, and nearby endpoints, returning JSON for bulk research, aggregate analysis, and record lookups without live-scraping each source platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to query Crawlora's hosted public datasets for market scans, population-level counts, faceted breakdowns, bulk lists, and single-record lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataset queries, filters, and POST bodies are sent to Crawlora under the user's API key.

Mitigation: Use the skill only when that data sharing is acceptable, and avoid sending sensitive private data in queries or request bodies.

Risk: The Crawlora API key could be exposed through logs, screenshots, commits, or shared outputs.

Mitigation: Keep CRAWLORA_API_KEY in the environment and out of logs, screenshots, commits, and shared transcripts.

Risk: Hosted datasets are refreshed on a schedule and should not be treated as real-time source-of-truth data.

Mitigation: Check the dataset context before making time-sensitive claims, and prefer live platform-specific lookups when the task requires current single-record data.

Risk: Search results are paginated, so a single page can undercount or miss later records.

Mitigation: Walk pages within documented limits when the user needs complete coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; Crawlora API results are paginated and reflect hosted dataset refresh schedules.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

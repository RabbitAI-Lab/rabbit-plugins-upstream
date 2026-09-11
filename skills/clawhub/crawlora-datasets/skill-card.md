## Description:

Queries Crawlora's pre-built hosted datasets through search, facets, item, and nearby endpoints, returning JSON for bulk analysis, aggregate research, filtered search, and dataset-record lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to query Crawlora's hosted public datasets for population-level research, faceted analysis, bulk list retrieval, and single-record dataset lookups without live-crawling each source platform.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Crawlora API key are sent to Crawlora's external API.

Mitigation: Use the skill only when that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and avoid hardcoding or committing credentials.

Risk: Some endpoints may return public contact information that could be misused for spam, harassment, doxxing, or bulk unsolicited outreach.

Mitigation: Confirm a legitimate user purpose before requesting contact fields and avoid workflows that enable abusive outreach or personal-data misuse.

Risk: Hosted datasets are refreshed on a schedule rather than in real time.

Mitigation: Use the results for dataset-level research and prefer a live platform-specific lookup when the user needs the current state of a single record.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results are paginated and dataset freshness follows Crawlora's refresh schedule.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

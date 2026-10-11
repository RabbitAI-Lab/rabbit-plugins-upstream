## Description:

Compare reported institutional-manager 13F holdings using Crawlora's SEC and stored-position tools while preserving filing coverage, security classes, and value units.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and researchers use the skill to compare reported institutional 13F positions, assess portfolio concentration or overlap, and identify possible issuer holders while retaining filing and coverage caveats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and the Crawlora API key are sent to the Crawlora API; requests may consume credits.

Mitigation: Use a scoped, private key; limit queries to the needed scope and monitor credit usage.

Risk: Delayed or incomplete 13F filings can be mistaken for current or complete holdings.

Mitigation: Show report and filing dates, truncation and coverage, and avoid presenting reported positions as live trades or complete portfolios.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/institutional-ownership-research)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with comparable position rows and disclosed calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes manager identity, filing dates, data coverage, value-unit assumptions, and unresolved joins.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

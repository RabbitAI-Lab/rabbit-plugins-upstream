## Description:

Enrich known prospects from LinkedIn profile URLs, slugs, or names with role and experience data via Veezee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enrich lead, prospect, or candidate lists when they already have LinkedIn identifiers or names and need current role, company, and recent experience summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospect identifiers are sent to Veezee during enrichment.

Mitigation: Confirm that using Veezee for LinkedIn data enrichment fits the user's privacy and compliance obligations before processing a batch.

Risk: The SDK or CLI may store a Veezee API key for reuse.

Mitigation: Review local credential storage and access controls before installing or running the integration.

Risk: Large batches can consume trial or paid credits.

Mitigation: Check usage before batches, monitor reported credits, and use per-call credit limits for larger runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veezee-build/skills/veezee-prospect-enrich)
- [Veezee LinkedIn MCP server](https://mcp.veezee.io/linkedin)
- [Veezee API key mint endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown report with per-prospect summaries and credit totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports name, current title, current company, two recent experience entries, and summed credits charged.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

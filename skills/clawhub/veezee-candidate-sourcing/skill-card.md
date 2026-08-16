## Description:

Find LinkedIn candidates matching a role spec, shortlist them, and enrich the shortlist with current role and experience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters, sourcers, hiring managers, and recruiting agents use this skill to convert role criteria into ranked LinkedIn candidate shortlists with current role and recent experience context. It is intended for candidate sourcing and profile enrichment, not contact-detail lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recruiting search criteria and LinkedIn profile lookups are sent to Veezee.

Mitigation: Install and use the skill only for recruiting workflows where sending those queries to Veezee is acceptable.

Risk: The SDK, CLI, or MCP connection may store a reusable Veezee API key.

Mitigation: Protect the API key as a credential and use normal credential rotation or revocation practices if access changes.

Risk: Candidate searches and profile enrichment consume credits, and batch enrichment can exhaust the free daily budget or paid balance.

Mitigation: Check usage before sourcing, set per-call credit limits for larger batches, and stop when budget or trial-cap errors occur.

Risk: Private LinkedIn profiles cannot be enriched and the skill does not provide emails or phone numbers.

Mitigation: Skip anonymous profiles during enrichment, report them separately as private matches, and avoid presenting the output as contact-ready outreach data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veezee-build/skills/veezee-candidate-sourcing)
- [Veezee publisher profile](https://clawhub.ai/user/veezee-build)
- [Veezee LinkedIn MCP server](https://mcp.veezee.io/linkedin)
- [Veezee all-tools MCP server](https://mcp.veezee.io/all)
- [Veezee API key mint endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown shortlist with candidate fields, skipped-profile notes, and credit usage summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranks candidates by fit and reports name, current title, current company, two recent experience entries, private-profile skips, and total credits spent.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

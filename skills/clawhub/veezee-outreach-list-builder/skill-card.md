## Description:

Turns a role or ICP spec into a ranked outbound sales list of LinkedIn prospects, each enriched with company context and a one-line personalized opener rationale.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and go-to-market users use this skill to convert an ICP, buyer role, or target-account description into a prioritized LinkedIn prospect list with company context and grounded opener rationales.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prospecting criteria and requested LinkedIn enrichment lookups are sent to Veezee, and SDK or CLI setup may store a Veezee API key for reuse.

Mitigation: Use managed secret storage where available, avoid submitting sensitive internal targeting data unless approved, and review the Veezee integration before installation.

Risk: Large lists and enrichment steps can consume credits quickly.

Mitigation: Check usage before starting, set max_credits on calls in larger batches, and review credit usage before running larger lists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veezee-build/skills/veezee-outreach-list-builder)
- [Veezee LinkedIn MCP endpoint](https://mcp.veezee.io/linkedin)
- [Veezee all-tools MCP endpoint](https://mcp.veezee.io/all)
- [Veezee API key mint endpoint](https://api.veezee.io/v1/keys/mint)

## Skill Output:

**Output Type(s):** [markdown, guidance, API calls, configuration]

**Output Format:** [Markdown ranked list with per-prospect notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes company context, opener rationale, private-profile skips, and total credits spent; does not include email addresses, phone numbers, or outreach sending.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

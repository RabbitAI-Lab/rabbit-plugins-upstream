## Description:

Deep research on one target company before outreach, covering company facts, key people, and recent posts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[veezee-build](https://clawhub.ai/user/veezee-build)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, partnerships, recruiting, and customer-facing teams use this skill to prepare a point-in-time LinkedIn-based account briefing before outreach or a meeting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target company names, URLs, domains, and selected person identifiers are sent to Veezee.

Mitigation: Use the skill only when Veezee is approved for that data, and avoid confidential target lists unless that approval is in place.

Risk: The Veezee API key may be stored by the SDK, CLI, or MCP connection.

Mitigation: Review where the key is stored in the chosen environment and apply normal credential handling controls.

Risk: A full account briefing can exceed the free daily credit budget.

Mitigation: Check usage before calls, set max_credits on calls, and stop for user approval when credit-limit or upgrade errors occur.

Risk: The workflow provides LinkedIn-only, point-in-time account research and does not return contact details.

Mitigation: Tell users when requests for email, phone numbers, other platforms, or ongoing monitoring are outside this skill's capability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/veezee-build/skills/veezee-account-research)
- [Veezee LinkedIn MCP server](https://mcp.veezee.io/linkedin)
- [Veezee all-tools MCP server](https://mcp.veezee.io/all)
- [Veezee key mint endpoint](https://api.veezee.io/v1/keys/mint)
- [Veezee upgrade page](https://veezee.io/upgrade)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown briefing with concise account facts, recent-post summary, key people, and credits spent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to one target account and LinkedIn data; the skill does not provide email addresses, phone numbers, or ongoing monitoring.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

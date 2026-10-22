## Description:

Negotiate terms with another person or their agent through Taasky for meetings, visits, shift swaps, prices, dates, and other agreements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill with an agent to negotiate terms with another person, such as meeting times, visits, shift swaps, or prices. The agent gathers the human’s limits, exchanges proposals, and guides the user through required confirmations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instruction updates and status checks may lead to offers without the human’s intended authorization.

Mitigation: Require approval for instruction updates and explicitly define when the agent may send offers.

Risk: Negotiations share private terms and limits, while room tokens grant access to a negotiation.

Mitigation: Share only the intended negotiation details and protect stored room tokens as credentials.

Risk: Recurring check-back jobs may act with their configured tools.

Mitigation: Approve recurring jobs and the tools they can use before enabling them.

## Reference(s):

- [Taasky](https://taasky.ai)
- [Taasky MCP server](https://mcp.taasky.ai/mcp)
- [Taasky OpenClaw integration](https://docs.taasky.ai/integrations/openclaw)
- [ClawHub Taasky release](https://clawhub.ai/marina-aronchik/skills/taasky)

## Skill Output:

**Output Type(s):** [API calls, Guidance, Text]

**Output Format:** [Structured Taasky MCP tool calls and concise user-facing text or Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Taasky MCP server; acceptance, rejection, and withdrawal require human confirmation.]

## Skill Version(s):

0.3.12 (source: server-resolved release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

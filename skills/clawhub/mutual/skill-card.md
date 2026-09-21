## Description:

Network for your human on Mutual, an introductions network where agents flag privately and two people decide. Register them, flag people worth meeting, check back for new arrivals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evannison](https://clawhub.ai/user/evannison)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to register a human on Mutual, discover redacted candidate cards, flag genuinely useful introductions, and report match status back to the human. It is intended for agent-assisted networking where humans retain control over whether introductions proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send personal profile details to mutualintro.com during registration, invitation, flagging, or polling.

Mitigation: Require the agent to show the exact destination and request body before any Mutual API call, and proceed only after user approval.

Risk: The skill points agents to mutable remote instructions as a source of truth.

Mitigation: Do not allow remote documentation to override the packaged skill, the user's instructions, or normal safety checks.

Risk: The MUTUAL_API_KEY bearer token can authorize later Mutual API actions.

Mitigation: Store the token only where the user expects it, avoid exposing it in conversation logs, and confirm before using it for follow-up requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evannison/skills/mutual)
- [Mutual homepage](https://mutualintro.com)
- [Mutual agent instructions](https://mutualintro.com/llms.txt)
- [Mutual OpenAPI specification](https://mutualintro.com/openapi.json)
- [Mutual MCP endpoint](https://mutualintro.com/api/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses curl and an optional MUTUAL_API_KEY bearer token for Mutual API calls.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

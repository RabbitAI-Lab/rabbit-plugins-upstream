## Description:

Turns an agent skill folder or repository into a varg how-to listing, checks it against the varg media standard, and submits it for review after the user approves the exact card.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill authors use this agent to check an Agent Skill against the varg media standard, prepare its public listing, and submit the reviewed listing for approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting a public listing without checking its details could publish incorrect or misleading information.

Mitigation: Review the exact card and its public links, then approve the card before submission.

Risk: Publishing uses the user's varg account credentials.

Mitigation: Use a reviewed installer version and install only this skill unless the optional collection is needed.

## Reference(s):

- [varg how-to publish guide](https://varg.ai/how-to/publish)
- [varg MCP server](https://mcp.varg.ai/mcp)
- [varg skill submissions API](https://api.varg.ai/v2/skills/submissions)
- [ClawHub skill listing](https://clawhub.ai/vargai/skills/varg-publish-skill)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, API Calls]

**Output Format:** [A varg listing card with review guidance, plus an optional submission through the varg MCP server or API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The user reviews and approves the exact listing before submission.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

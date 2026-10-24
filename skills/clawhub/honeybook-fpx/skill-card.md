## Description:

Guides agents in capturing a signed-in HoneyBook session and using shell requests to retrieve client-portal data without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and HoneyBook client-portal users can retrieve contracts, invoices, proposals, payment methods, and workspace status through shell commands without running an MCP server. The skill also describes a separate message-sending action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The session capture exposes live HoneyBook credentials.

Mitigation: Review credential access before installing and avoid keeping captured session JSON or tokens in shared locations, shell history, logs, or screenshots.

Risk: The message-sending workflow can contact real vendors despite the skill's read-oriented description.

Mitigation: Treat message sending as a write action and review and confirm its recipient and contents before execution.

## Reference(s):

- [HoneyBook request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [Fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/honeybook-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API reads return HoneyBook data; the separate message workflow can contact a vendor.]

## Skill Version(s):

1.2.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

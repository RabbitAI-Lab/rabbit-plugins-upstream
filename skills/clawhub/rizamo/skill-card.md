## Description:

Publish and schedule social media posts on Instagram, Facebook, TikTok, YouTube and Threads with Rizamo, see how they did, and answer comments and messages. Use when the user wants to post or schedule social content, check post or account analytics, or reply to their audience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agrafador](https://clawhub.ai/user/agrafador)

### License/Terms of Use:

MIT-0

## Use Case:

Social media managers, creators, and brand teams use the skill to prepare and publish or schedule posts across connected social accounts, review analytics, and respond to audience comments and messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth or an API key can authorize access to connected Rizamo profiles and social accounts.

Mitigation: Connect only the profiles the user intends the agent to use, and provide an API key only when needed; it is optional when the Rizamo MCP server is connected.

Risk: Publishing or replying can send content to an external audience, and scheduled posts publish automatically.

Mitigation: Show the proposed content and wait for approval before publishing, scheduling, or sending a reply; create posts as drafts until approved.

## Reference(s):

- [Rizamo agent connection guide](https://docs.rizamo.com/connect-an-agent)
- [Rizamo API documentation](https://docs.rizamo.com/api)
- [Rizamo ClawHub release](https://clawhub.ai/agrafador/skills/rizamo)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with API request examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

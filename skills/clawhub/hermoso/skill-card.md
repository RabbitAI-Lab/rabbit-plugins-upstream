## Description:

Run marketing from your agent - research winning ads, make finished image and video ads, publish, schedule and run ad campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hermoso-dev](https://clawhub.ai/user/hermoso-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to connect an agent to Hermoso's marketing MCP for ad research, creative generation, publishing, scheduling, and paused ad campaign setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a Hermoso token and connected social or ad accounts.

Mitigation: Keep the token in the user's MCP configuration or environment secret storage, and use connected accounts only for user-requested actions.

Risk: Renders and campaign builds can consume paid credits.

Mitigation: Call the live capabilities or credits tools and quote costs before starting a render or campaign build.

Risk: Publishing and scheduling tools can create public posts on connected channels.

Mitigation: Confirm the destination channel, content, and timing with the user before publishing or scheduling.

Risk: Ad budget can move if status-changing tools are called with explicit confirmation.

Mitigation: Leave campaigns paused by default and pass confirm:true only after the user explicitly asks to go live.

## Reference(s):

- [Hermoso MCP homepage](https://hermoso.ai/mcp/)
- [Hermoso app](https://app.hermoso.ai)
- [Hermoso ClawHub skill page](https://clawhub.ai/hermoso-dev/skills/hermoso)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Media assets]

**Output Format:** [Markdown guidance with inline shell commands, MCP tool names, hosted asset URLs, and campaign status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include credit quotes, render job IDs, connector status, scheduled post details, and paused campaign identifiers.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

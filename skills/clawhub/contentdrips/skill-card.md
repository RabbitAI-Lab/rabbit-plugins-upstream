## Description:

Connects OpenClaw to ContentDrips MCP for social media design creation, carousel and graphic generation, and publishing workflows for LinkedIn and Instagram.

This skill is ready for commercial/non-commercial use.

## Publisher:

[usama-gh](https://clawhub.ai/user/usama-gh)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect OpenClaw with ContentDrips, create or update social media graphics and carousels, and manage publishing or scheduling after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing, scheduling, or deleting social media content may affect a user's connected ContentDrips and social accounts.

Mitigation: Require explicit user confirmation for publish, schedule, and delete actions, including the named platforms before tool execution.

Risk: The ContentDrips API token grants access to account workflows.

Mitigation: Keep the API token scoped and protected, prefer the CONTENTDRIPS_API_KEY environment variable, and avoid exposing secrets in shared output.

Risk: Content may be sent to the wrong workspace or platform if the agent assumes defaults.

Mitigation: Fetch profiles and connected social accounts first, ask when multiple workspaces or styles are available, and set only the platform flags the user explicitly requested.

## Reference(s):

- [ClawHub ContentDrips skill page](https://clawhub.ai/usama-gh/skills/contentdrips)
- [ContentDrips](https://contentdrips.com)
- [ContentDrips MCP server](https://mcp.contentdrips.com/mcp)
- [Manual JSON examples](examples.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown instructions with inline bash commands, MCP tool guidance, editor links, and JSON examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ContentDrips editor links, export URLs, and platform-specific publish or schedule confirmations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides agents through Box authentication, tool selection, content workflows, and troubleshooting using MCP, CLI, or REST where appropriate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iskysun96](https://clawhub.ai/user/iskysun96)

### License/Terms of Use:

MIT-0

## Use Case:

Box users and developers use this skill to choose and configure Box tools, find and manage content, collaborate, and diagnose access or API errors while keeping actions scoped to the task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Box tools can access or change account content beyond the intended task.

Mitigation: Use least-privilege Box apps and limit actions to the necessary files, folders, and acting identity.

Risk: Sharing, collaborator changes, and bulk or metadata operations can expose or alter content at scale.

Mitigation: Confirm the audience, scope, and planned changes before acting; verify the results afterward.

Risk: Credentials or sensitive documents may be exposed through chat, downloads, or external processing.

Mitigation: Keep secrets out of chat, prefer Box-native processing, and seek explicit approval before local downloads or sensitive-content processing.

Risk: Direct REST fallback may bypass the user's expected tool and authorization flow.

Mitigation: Use MCP or CLI when available and obtain explicit confirmation before direct REST fallback.

## Reference(s):

- [Box skill release](https://clawhub.ai/iskysun96/skills/box)
- [Box MCP tools](https://docs.box.com/en/box-mcp/tools)
- [Box developer guides](https://developer.box.com/guides)
- [Box API reference](https://developer.box.com/reference)
- [Box CLI guidance](references/box-cli.md)
- [Box security guardrails](references/guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on available Box tooling, permissions, and user confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

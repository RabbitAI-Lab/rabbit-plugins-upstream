## Description:

Router skill for PostKing — confirms the active brand, then hands off to the right specialist skill for posts, blogs, landing pages, SEO, or setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitsandtea](https://clawhub.ai/user/bitsandtea)

### License/Terms of Use:

MIT-0

## Use Case:

External PostKing users and agents use this skill as the starting point for PostKing work: it confirms the active brand, checks account connectivity, and routes the request to the specialist skill for the requested content or setup task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through PostKing authentication, including legacy password-based CLI flags.

Mitigation: Prefer device-code or magic-link login flows and avoid pasting passwords or API keys into prompts when possible.

Risk: Brand-scoped actions can affect the wrong PostKing workspace if the active brand is incorrect.

Mitigation: Confirm the active brand before publishing, scheduling, billing, or deleting content.

Risk: Some referenced PostKing commands can publish, schedule, purchase credits, subscribe to plans, or delete resources.

Mitigation: Review billing, publishing, scheduling, and destructive commands before allowing an agent to run them.

## Reference(s):

- [pking command reference](references/commands.md)
- [Installing postking-cli](references/install.md)
- [PostKing MCP endpoint](https://mcp.postking.app/mcp)
- [ClawHub skill page](https://clawhub.ai/bitsandtea/skills/postking-getting-started)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline MCP tool calls and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to specialist PostKing skills and may surface PostKing dashboard URLs returned by commands.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

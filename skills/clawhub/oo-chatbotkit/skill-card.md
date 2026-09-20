## Description:

ChatBotKit (chatbotkit.com). Use this skill for ANY ChatBotKit request: reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage ChatBotKit bots, conversations, datasets, files, usage data, and related account resources through the OOMOL oo CLI. It supports read workflows as well as confirmed write and destructive workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on OOMOL's oo CLI and an OOMOL-connected ChatBotKit account, which grants account access through that toolchain.

Mitigation: Install and use the skill only if the user trusts OOMOL's oo CLI and is comfortable granting it access to the connected ChatBotKit account.

Risk: Write and destructive ChatBotKit actions can change bots, datasets, files, conversations, or attached data.

Mitigation: Review the live action schema, exact target, payload, and expected effect with the user before approving any write or destructive action.

## Reference(s):

- [ChatBotKit homepage](https://chatbotkit.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chatbotkit)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before payload construction; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

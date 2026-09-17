## Description:

AgentMail (agentmail.to) helps an agent read, create, update, and delete AgentMail data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to manage AgentMail inboxes, messages, threads, drafts, domains, pods, webhooks, API keys, allow/block lists, and metrics from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete AgentMail resources, including messages, inboxes, domains, webhooks, API keys, pods, and allow/block lists.

Mitigation: Require explicit user confirmation for write and destructive actions, including the exact target and payload, before running the corresponding oo CLI command.

Risk: The fallback setup includes remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run remote installer commands unless the installer source has been independently verified and the user explicitly approves the installation.

## Reference(s):

- [AgentMail homepage](https://agentmail.to)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub AgentMail skill](https://clawhub.ai/oomol/skills/oo-agent-mail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return AgentMail connector JSON responses and execution identifiers when actions are run.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

AgentMail helps agents read, create, update, and delete AgentMail resources through the OOMOL agent_mail connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage AgentMail inboxes, messages, drafts, domains, pods, webhooks, API keys, metrics, and organization identity from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands for the oo CLI could execute unverified shell code if run automatically.

Mitigation: Install or update the oo CLI only through a verified, user-controlled process before allowing the skill to run connector actions.

Risk: Send, API key, webhook, write, and destructive actions can change AgentMail state or expose access.

Mitigation: Confirm the exact payload, target resource, and intended effect with the user before running those actions.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema before constructing payloads so commands match the current AgentMail contract.

## Reference(s):

- [AgentMail homepage](https://agentmail.to)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub AgentMail skill](https://clawhub.ai/oomol/skills/oo-agent-mail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when --json is used; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.5 (source: frontmatter and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

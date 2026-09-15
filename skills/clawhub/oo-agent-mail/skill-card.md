## Description:

AgentMail (agentmail.to) helps an agent read, search, create, update, send, and delete AgentMail resources through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage AgentMail inboxes, messages, drafts, domains, pods, webhooks, API keys, metrics, and allow or block lists from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer payload before execution and prefer a verified manual installation path for the oo CLI.

Risk: The skill can send messages, create resources, update labels, manage API keys and webhooks, and delete AgentMail data.

Mitigation: Confirm the exact payload, target resource, and expected effect before any write or destructive action.

Risk: The security verdict is suspicious because of unverified remote installer scripts.

Mitigation: Install only when the user trusts OOMOL and the oo CLI, and avoid letting an agent run curl-to-shell or PowerShell download-to-execute commands directly.

## Reference(s):

- [AgentMail homepage](https://agentmail.to)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-agent-mail)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; state-changing and destructive actions require confirmation.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

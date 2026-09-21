## Description:

Vapi helps agents manage Vapi resources through an OOMOL-connected CLI connector for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live Vapi action schemas and run Vapi connector actions for assistants, phone numbers, calls, chats, sessions, evaluations, scorecards, policies, files, and provider resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts without verification.

Mitigation: Review setup before installing and prefer an official, verifiable oo CLI package or installer.

Risk: Write and destructive Vapi actions can change or delete resources.

Mitigation: Inspect the live action schema and confirm the exact payload, target resource, and effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-vapi)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Vapi homepage](https://vapi.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include live schema inspection steps, connector command payloads, and summarized Vapi API responses.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

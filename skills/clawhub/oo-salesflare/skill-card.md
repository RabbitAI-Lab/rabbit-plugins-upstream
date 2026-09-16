## Description:

Use this skill for Salesflare CRM requests that read, create, or update data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and operations users can ask an agent to inspect Salesflare schemas and run Salesflare account, contact, opportunity, task, and current-user actions. The skill supports read workflows and user-confirmed write workflows through an OOMOL-connected Salesflare account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes a one-line remote installer executed directly in a shell.

Mitigation: Prefer a verified or package-manager installation method for the oo CLI, or review the installer source before running it.

Risk: The skill uses OOMOL as an intermediary for Salesflare actions and server-side credentials.

Mitigation: Install only when the user is comfortable with OOMOL brokering Salesflare actions for the connected account.

Risk: Several actions create or update Salesflare CRM records.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [ClawHub Salesflare skill page](https://clawhub.ai/oomol/skills/oo-salesflare)
- [Salesflare homepage](https://salesflare.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Salesflare action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

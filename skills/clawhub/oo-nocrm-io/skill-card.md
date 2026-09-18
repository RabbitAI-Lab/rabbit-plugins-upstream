## Description:

Operate noCRM.io through an OOMOL-connected account for reading, creating, updating, and deleting CRM data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and CRM operators use this skill to have an agent inspect noCRM.io connector schemas and run lead-management actions through the oo CLI with OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsafe pipe-to-shell installer commands may be proposed during setup.

Mitigation: Install the oo CLI only through a verified manual process; do not let an agent run installer commands automatically.

Risk: CRM write actions can change lead state, ownership, tags, descriptions, reminders, or duplicate records.

Mitigation: Require explicit user confirmation of the exact payload and intended effect before running any write action.

Risk: Destructive lead deletion can remove CRM records.

Mitigation: Require explicit approval for the specific target lead before running delete_lead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nocrm-io)
- [noCRM.io homepage](https://www.nocrm.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; CRM write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

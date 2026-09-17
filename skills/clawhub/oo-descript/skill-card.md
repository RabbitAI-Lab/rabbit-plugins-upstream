## Description:

Descript (descript.com). Use this skill for Descript requests that read, create, or update data through the OOMOL `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Descript projects from an OOMOL-connected account, including listing projects and jobs, importing media, prompting Underlord, publishing compositions, and retrieving share or download links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer one-liners for the OOMOL oo CLI that could execute arbitrary code if run without review.

Mitigation: Do not let an agent run those installer commands automatically; review the installer or use a safer verified installation method before enabling the skill.

Risk: Write actions can change Descript project state, including importing media, prompting Underlord edits, publishing projects, or canceling jobs.

Mitigation: Confirm the exact payload, project, composition, and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-descript)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Descript Homepage](https://www.descript.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect live action schemas before execution and require user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

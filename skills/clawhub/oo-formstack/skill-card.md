## Description:

Formstack (formstack.com). Use this skill for ANY Formstack request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Formstack through an OOMOL-connected account, including listing forms and submissions, retrieving form details, and creating, updating, or deleting submissions with explicit confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell and PowerShell installer commands that could execute arbitrary code if followed blindly.

Mitigation: Install the oo CLI only from a trusted, verified source and review the installer or use the documented install guide before execution.

Risk: Formstack write and destructive actions can change or permanently delete submissions and associated data.

Mitigation: Confirm the exact action, target form or submission, and payload with the user before running write or deletion commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-formstack)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Formstack homepage](https://www.formstack.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Greenhouse (greenhouse.com). Use this skill for ANY Greenhouse request: reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to operate Greenhouse through an OOMOL-connected account, including retrieving candidates, applications, and jobs and adding candidate activity feed notes. The skill is intended for Greenhouse workflows that need schema-checked connector actions rather than direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that may be unsafe if run without review.

Mitigation: Verify OOMOL's installer source before use, or prefer an official package manager, signed release, checksum-verified download, or manual installer review.

Risk: Greenhouse read actions can expose sensitive HR data.

Mitigation: Confirm that the user has appropriate access before retrieving candidate, application, job, or activity feed data.

Risk: Adding candidate notes changes Greenhouse state and records an On-Behalf-Of audit user.

Mitigation: Confirm the exact note payload, target candidate, and audit user with the user before running the write action.

## Reference(s):

- [ClawHub Greenhouse skill page](https://clawhub.ai/oomol/skills/oo-greenhouse)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Greenhouse homepage](https://www.greenhouse.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Greenhouse connector commands that return JSON responses.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

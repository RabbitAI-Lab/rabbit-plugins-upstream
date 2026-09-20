## Description:

Formstack lets agents read, create, update, and delete Formstack data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Formstack forms and submissions through an OOMOL-connected Formstack account, including listing forms, reading submissions, creating submissions, updating records, and deleting submissions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path uses direct remote script execution for installing the oo CLI.

Mitigation: Review the installer source and prefer a verified installer, checksum, signature, or package-manager flow before installation.

Risk: The skill can create, update, and permanently delete live Formstack submissions.

Mitigation: Confirm the target form or submission, exact payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Formstack Skill](https://clawhub.ai/oomol/skills/oo-formstack)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formstack](https://www.formstack.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

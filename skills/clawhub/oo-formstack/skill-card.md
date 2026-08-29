## Description:

Operate Formstack (formstack.com) through OOMOL for reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Formstack through an OOMOL-connected account, including reading forms, fields, and submissions and creating, updating, or deleting submissions after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update live Formstack submissions.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

Risk: The skill can permanently delete Formstack submissions and associated data.

Mitigation: Confirm the target submission and obtain explicit approval before destructive actions.

Risk: The skill operates a user's Formstack account through OOMOL-managed credentials.

Mitigation: Install and use it only when OOMOL is intended to operate that Formstack account, and review payloads before approval.

## Reference(s):

- [Formstack homepage](https://www.formstack.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The oo CLI returns connector responses as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

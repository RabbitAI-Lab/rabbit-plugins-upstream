## Description:

Formsite (formsite.com). Use this skill for ANY Formsite request — reading, creating, updating, and deleting data. Whenever a task involves Formsite, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Formsite through an OOMOL-connected account, including reading forms and results and managing Formsite webhooks through the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts, which the security evidence flags as suspicious if executed without verification.

Mitigation: Prefer a verified package or inspect and validate the installer before execution.

Risk: Write and destructive Formsite actions can change or delete account data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Formsite Skill](https://clawhub.ai/oomol/skills/oo-formsite)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Formsite homepage](https://www.formsite.com)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the oo CLI connector when run with --json.]

## Skill Version(s):

1.0.3 (source: artifact metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

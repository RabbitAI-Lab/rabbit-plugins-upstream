## Description:

Operate Plunk through an OOMOL-connected account for reading, creating, updating, deleting, emailing, event tracking, and email verification workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Plunk contacts, transactional emails, event tracking, and email verification through the oo CLI with an OOMOL-connected Plunk account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer one-liners may execute unverified installation code.

Mitigation: Review and verify the oo CLI source and installer path before running remote installer commands.

Risk: Plunk actions can change state by creating or updating contacts, deleting contacts, sending emails, or tracking events.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub Plunk Skill](https://clawhub.ai/oomol/skills/oo-plunk)
- [Plunk Homepage](https://www.useplunk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

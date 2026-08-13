## Description:

Appcircle (appcircle.io). Use this skill for ANY Appcircle request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Appcircle organizations and profile data through an OOMOL-connected account. It supports schema-first CLI execution for read-only Appcircle connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected Appcircle account.

Mitigation: Install or reconnect those dependencies only when a command fails with a matching CLI, authentication, connection, scope, expiration, or billing error.

Risk: Future connector actions marked write or destructive could change or remove Appcircle data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-appcircle)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Appcircle Homepage](https://appcircle.io/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are described as JSON containing data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

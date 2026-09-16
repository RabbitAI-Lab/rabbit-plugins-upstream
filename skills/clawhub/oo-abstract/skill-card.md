## Description:

Abstract lets agents validate email addresses through Abstract API using an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run Abstract email validation through OOMOL-managed credentials, including deliverability, quality, and risk checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute code on the user's machine.

Mitigation: Review the oo CLI installation path before installing; prefer an official package or verified release with checksum or signature validation, and do not let an agent run downloaded installer scripts automatically unless the installer source and machine context are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-abstract)
- [Abstract homepage](https://www.abstractapi.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include connector data and an execution ID when actions run successfully.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

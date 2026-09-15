## Description:

Eventee (eventee.co). Use this skill for Eventee searching and read-only event data retrieval through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Eventee event content, attendee groups, participants, registrations, and session reviews through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute a remote installer script directly through curl or PowerShell.

Mitigation: Prefer a verified oo CLI package or manually review the installer before execution.

Risk: Eventee data returned by the connector passes through OOMOL infrastructure.

Mitigation: Use the skill only when OOMOL is an approved processor for the Eventee data involved.

Risk: Future connector actions could change or delete Eventee data.

Mitigation: Require explicit user confirmation for any write or destructive action, including the exact payload and expected effect.

## Reference(s):

- [Eventee homepage](https://eventee.co)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eventee)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running Eventee read actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

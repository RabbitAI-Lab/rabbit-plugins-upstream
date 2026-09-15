## Description:

SimplyBook.me (simplybook.me) enables agents to read, create, and update SimplyBook.me data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate SimplyBook.me through the OOMOL oo CLI, inspect live connector schemas, and run booking-service actions through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands may execute unverified code during first-time oo CLI setup.

Mitigation: Prefer a verified package or download-then-verify process, and avoid elevated terminals unless the installer source has been independently verified.

Risk: Write-tagged SimplyBook.me actions can change account data if invoked with an incorrect payload.

Mitigation: Confirm the exact payload and expected effect with the user, then check the live connector schema before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-simplybook-me)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [SimplyBook.me](https://simplybook.me/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns JSON responses from oo CLI actions when executed.]

## Skill Version(s):

1.0.2 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

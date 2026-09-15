## Description:

AppleDB lets agents search and retrieve AppleDB device and operating system build records through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query AppleDB for Apple device records and operating system build records through validated connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer path before use, prefer a trusted version-pinned source with checksum or signature verification, and run only the listed AppleDB read actions unless future releases clearly document additional capabilities.

## Reference(s):

- [AppleDB homepage](https://appledb.dev)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-appledb)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live AppleDB action schemas before running connector requests.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

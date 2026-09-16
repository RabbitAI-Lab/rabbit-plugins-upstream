## Description:

Operate Drimify through an OOMOL-connected account to retrieve and list app data collection records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Drimify connector schemas and run read actions that retrieve or list Drimify app data collection records through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can lead an agent or user to run remote installer commands directly in a shell.

Mitigation: Require explicit approval before running installer commands, review the installer first, and prefer official version-pinned installation instructions.

Risk: Connector actions operate against a connected Drimify account.

Mitigation: Run read actions directly only when appropriate; require user confirmation for any action tagged write or destructive and verify payloads against the live schema first.

## Reference(s):

- [Drimify homepage](https://drimify.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, JSON payloads, setup guidance, and connector responses; live connector schemas should be inspected before action payloads are built.]

## Skill Version(s):

1.0.2 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

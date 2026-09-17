## Description:

Kadoa (kadoa.com). Use this skill for ANY Kadoa request — searching and reading data. Whenever a task involves Kadoa, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Kadoa through an OOMOL-connected account, including listing workflows, retrieving workflow configuration and execution status, reading extracted workflow data, and exporting matching workflow records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports that first-time setup includes unverified remote installer commands run directly in a shell.

Mitigation: Prefer official, versioned, signed, or checksum-verified OOMOL CLI installation instructions and avoid running pipe-to-shell commands from an elevated terminal.

## Reference(s):

- [Kadoa homepage](https://www.kadoa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kadoa)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; exported workflow records may be returned through a temporary signed download URL.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

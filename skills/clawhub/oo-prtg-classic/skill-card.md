## Description:

PRTG Classic supports searching and read-only data access through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and administrators use this skill to inspect PRTG Classic devices and sensors through OOMOL's connector-backed oo CLI workflow without directly handling raw PRTG tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes running an unverified remote installer directly.

Mitigation: Before installation, prefer a pinned release, package manager, or installer with publisher signature or checksum verification.

Risk: The skill reads PRTG Classic device and sensor data through an OOMOL-connected account.

Mitigation: Use an account scoped to the minimum PRTG Classic data needed for the task and keep credentials managed server-side through OOMOL.

## Reference(s):

- [PRTG Classic ClawHub Release](https://clawhub.ai/oomol/skills/oo-prtg-classic)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [PRTG Classic Homepage](https://www.paessler.com/prtg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides schema inspection and connector execution for read-only PRTG Classic device and sensor data.]

## Skill Version(s):

1.0.3 (source: artifact frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

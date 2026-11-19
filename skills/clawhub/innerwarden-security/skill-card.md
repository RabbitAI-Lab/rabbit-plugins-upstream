## Description:

Helps an OpenClaw owner install, verify, and manage InnerWarden protections for agent tools and MCP calls, with optional Linux host protection through Pro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maiconburn](https://clawhub.ai/user/maiconburn)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw owners and developers use the skill to install and verify InnerWarden, inspect protection status and command verdicts, and manage enforcement, upgrades, or removal. It also explains the limits of Community coverage and the optional Linux-only Pro host layer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with medium confidence because installation runs a remote script directly and three referenced files were unavailable to the scan.

Mitigation: Consider avoiding installation until the remote installer can be independently verified and the missing references can be reviewed.

## Reference(s):

- [InnerWarden documentation](https://github.com/InnerWarden/innerwarden-skill)
- [Pro server setup](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/pro-on-a-server.md)
- [Managing Pro](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/managing-pro.md)
- [Pro pricing](https://innerwarden.com/pricing)
- [InnerWarden ClawHub release](https://clawhub.ai/maiconburn/skills/innerwarden-security)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Version-aware installation, verification, and maintenance guidance.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

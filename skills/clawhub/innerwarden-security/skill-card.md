## Description:

Install, verify, and manage InnerWarden to help OpenClaw agents screen tool and MCP calls, with optional Linux host enforcement in Pro.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maiconburn](https://clawhub.ai/user/maiconburn)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw agent owners and developers use this skill to install and verify InnerWarden, inspect what it screens, review command verdicts, and manage monitor or enforce settings. It also explains the limits of Community coverage and Linux-only Pro host controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is marked suspicious because its install guidance runs a remotely fetched script directly; the available scan coverage is partial because three referenced local materials were missing.

Mitigation: Avoid installation unless the installer can be independently verified before it runs, and review the missing materials before relying on the scan evidence.

## Reference(s):

- [InnerWarden skill documentation](https://github.com/InnerWarden/innerwarden-skill)
- [Pro server setup](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/pro-on-a-server.md)
- [Managing InnerWarden Pro](https://github.com/InnerWarden/innerwarden-skill/blob/master/docs/managing-pro.md)
- [InnerWarden pricing](https://innerwarden.com/pricing)
- [ClawHub release page](https://clawhub.ai/maiconburn/skills/innerwarden-security)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

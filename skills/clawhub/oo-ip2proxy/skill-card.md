## Description:

IP2Proxy helps agents query the IP2Proxy service through OOMOL's oo CLI to inspect schemas and run proxy-detection lookups for IPv4 or IPv6 addresses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run read-only IP2Proxy lookups through an OOMOL-connected account, after checking the live connector schema and submitting a matching JSON payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that execute scripts directly, which is a high-impact local installation path without integrity checks.

Mitigation: Review the installer source before execution and prefer a pinned, signed, or checksum-verified installation path when available.

## Reference(s):

- [IP2Proxy ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-ip2proxy)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [IP2Proxy Homepage](https://www.ip2location.com/web-service/ip2proxy)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before running actions; normal lookup responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

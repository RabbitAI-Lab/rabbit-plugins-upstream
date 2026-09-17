## Description:

Cloudflare DNS supports reading, creating, updating, and deleting Cloudflare DNS data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cloudflare accounts, zones, and DNS records, then create, update, or delete DNS records through OOMOL-managed Cloudflare credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote oo CLI installer scripts without integrity checks.

Mitigation: Prefer a package manager or a downloaded, version-pinned installer with checksum or signature verification.

Risk: The skill can create, update, and delete Cloudflare DNS records.

Mitigation: Use least-privileged Cloudflare access and require explicit review of DNS write or delete payloads before execution.

## Reference(s):

- [Cloudflare DNS ClawHub listing](https://clawhub.ai/oomol/skills/oo-cloudflare-dns)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cloudflare](https://www.cloudflare.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI action schemas before constructing connector requests.]

## Skill Version(s):

1.0.5 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

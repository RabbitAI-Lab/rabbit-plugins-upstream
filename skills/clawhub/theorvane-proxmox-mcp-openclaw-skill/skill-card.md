## Description:

Install the immutable Proxmox MCP v0.1.1 GitHub Release locally and register it with OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sjungwon03](https://clawhub.ai/user/sjungwon03)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to install a pinned Proxmox MCP release, verify its checksum, and register the resulting stdio executable with OpenClaw.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OpenClaw MCP registration uses Proxmox API token values for ongoing MCP use.

Mitigation: Use a least-privilege Proxmox token, review where OpenClaw stores MCP environment variables, and remove the registration when it is no longer needed.

Risk: The installer downloads and registers a third-party Proxmox MCP release.

Mitigation: Install only after reviewing and trusting the referenced Proxmox MCP release and its checksum-verified archive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/sjungwon03/skills/theorvane-proxmox-mcp-openclaw-skill)
- [Publisher Profile](https://clawhub.ai/user/sjungwon03)
- [Theorvane/proxmox-mcp](https://github.com/Theorvane/proxmox-mcp)
- [Pinned Proxmox MCP v0.1.1 Release Archive](https://github.com/Theorvane/proxmox-mcp/releases/download/v0.1.1/proxmox-mcp-0.1.1.tar.gz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces installation and dry-run guidance for local OpenClaw MCP registration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

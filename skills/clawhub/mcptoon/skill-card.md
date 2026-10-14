## Description:

Helps agents discover, select, and call MCP tools efficiently while managing shared skill catalogs and finding relevant documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[activeing123](https://clawhub.ai/user/activeing123)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use mcptoon to reduce MCP tool-catalog overhead, choose and call relevant tools, share skill catalogs across agents, and locate relevant documents without reading entire directories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading an unpinned CLI may run software the user has not reviewed.

Mitigation: Request explicit approval before pip, pipx, uvx, npx, or quickstart commands; consider pinning the CLI version.

Risk: Gateway setup, synchronization, removal, or restore can change agent MCP configurations and skill catalogs.

Mitigation: Get approval before changes, preview them where possible, and review which configurations and skill views will be affected.

Risk: Compressed tool results retain originals in a local cache, potentially including sensitive content.

Mitigation: Review cache and configuration locations before use; retrieve originals when needed and disable compression if it is unsuitable.

## Reference(s):

- [mcptoon on ClawHub](https://clawhub.ai/activeing123/skills/mcptoon)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides tool discovery, calls, setup, and retrieval of compressed tool results.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

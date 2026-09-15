## Description:

WPS MCP (wps.cn) helps an agent read, create, update, list, search, and inspect WPS cloud documents through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate WPS MCP from an OOMOL-connected account, including reading documents, retrieving file metadata, listing and searching drives, and creating documents or folders when confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Prefer official, verifiable installation documentation or a trusted package manager, and run remote installer pipelines only after accepting the risk of executing mutable network code.

Risk: Write actions can create WPS files or folders in the connected account.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write operations.

## Reference(s):

- [WPS MCP ClawHub listing](https://clawhub.ai/oomol/skills/oo-wps-mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WPS homepage](https://www.wps.cn)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return WPS document content, spreadsheet cells, file metadata, folder listings, and execution metadata from the connected service.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

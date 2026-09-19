## Description:

WPS MCP (wps.cn) lets an agent read, create, update, list, search, and inspect WPS cloud files through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate WPS MCP through an authenticated OOMOL connector, including reading WPS files, creating documents or folders, discovering available WPS tools, and searching WPS cloud documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote shell installer commands that could be unsafe if run automatically or from an unverified source.

Mitigation: Do not let an agent run curl|bash or irm|iex installer commands automatically; install the oo CLI only from a trusted, verified source.

Risk: WPS MCP write or destructive actions can change documents, folders, or other connected WPS state.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or destructive WPS actions.

## Reference(s):

- [WPS MCP homepage](https://www.wps.cn)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WPS MCP ClawHub page](https://clawhub.ai/oomol/skills/oo-wps-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands and JSON request payloads for WPS MCP actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Cloudflare MCP lets agents operate Cloudflare's MCP connector through the OOMOL oo CLI to search documentation, discover API endpoints, and run Cloudflare MCP actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to interact with Cloudflare MCP through an OOMOL-connected account, including searching Cloudflare documentation, inspecting action schemas, discovering API parameters, and running connector actions with JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The execute action may affect Cloudflare account state when used with non-read-only endpoints or payloads.

Mitigation: Inspect the live action schema first and require explicit user confirmation for any endpoint or payload that is not clearly read-only.

Risk: The setup guidance includes pipe-to-shell CLI installation commands.

Mitigation: Confirm trust in OOMOL's CLI installer before installation and prefer a verified or package-manager installation path when available.

## Reference(s):

- [Cloudflare MCP homepage](https://github.com/cloudflare/mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudflare-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, action schema inspection steps, JSON request payloads, setup guidance, and confirmation prompts for actions that can change Cloudflare account state.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

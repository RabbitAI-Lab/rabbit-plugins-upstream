## Description:

Sorftime MCP lets agents search and read marketplace product, keyword, category, market, and trend data through an OOMOL-connected Sorftime account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research marketplace products, categories, keywords, and trends across Sorftime-supported commerce platforms from a connected Sorftime account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may use remote installer scripts from OOMOL-controlled URLs.

Mitigation: Use a verified oo CLI installation method, inspect installer sources where possible, and avoid running remote scripts from an elevated shell.

Risk: The generic call_tool action can change or delete account data or spend credits without action-specific confirmation tags.

Mitigation: Confirm the exact tool name, payload, effect, and expected credit cost with the user before running call_tool or any write-like action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sorftime-mcp)
- [Sorftime MCP homepage](https://www.sorftime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and execution metadata when actions are run.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

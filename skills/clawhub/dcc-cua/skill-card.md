## Description:

Control application UI through project-owned DCC-CUA for explicit DCC-CUA requests, including browsers and non-DCC apps, or as a DCC-MCP UI fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users directing an agent use this skill to control a specifically identified DCC application, browser, or desktop window through DCC-CUA and verify the resulting state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: UI automation could act on an unintended application or window.

Mitigation: Grant narrowly scoped tasks, confirm the exact process and window binding before input, and verify the final state.

Risk: Authenticated sessions, purchases, security settings, and permission prompts can have sensitive consequences.

Mitigation: Keep these actions behind human confirmation and stop at unexpected authentication or permission prompts.

## Reference(s):

- [DCC-CUA skill homepage](https://github.com/dcc-mcp/dcc-mcp-agent-plugins/blob/main/plugins/dcc-mcp/skills/dcc-cua/SKILL.md)
- [DCC host commands](references/DCC_HOST.md)
- [Browser and desktop binding](references/BROWSER_AND_DESKTOP.md)
- [Continuity and evidence epochs](references/CONTINUITY.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown and plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports target binding, verified outcomes, or a concrete blocker.]

## Skill Version(s):

0.19.108 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

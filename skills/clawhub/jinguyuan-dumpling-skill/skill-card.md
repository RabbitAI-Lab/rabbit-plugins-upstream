## Description:

This skill helps agents answer questions about Jinguyuan Dumpling Restaurant locations, hours, queue status, recommended dishes, takeout, raw dumpling pickup, and online queue actions through the bundled CLI and official restaurant API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jinguyuan](https://clawhub.ai/user/jinguyuan)

### License/Terms of Use:

MIT

## Use Case:

External restaurant customers and their agents use this skill to get current Jinguyuan Dumpling Restaurant information, queue guidance, pickup information, and restaurant news. When explicitly requested and confirmed, the skill can also guide real online queue actions such as taking a number, checking personal queue progress, or canceling a queue order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queue features use Meituan authorization, store a local token under ~/.jinguyuan, and the signing dependency creates a persistent ~/.cliguard device identifier that the skill does not clearly disclose.

Mitigation: Review the skill before installing if local account authorization helpers are uncomfortable; proceed only when the publisher is trusted and the local token and device identifier behavior is acceptable.

Risk: Confirmed take-number and cancel operations affect a real queue account.

Mitigation: Use these actions only after the user gives explicit confirmation for the current request, and verify queue status with the CLI or Meituan account if an operation result is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jinguyuan/skills/jinguyuan-dumpling-skill)
- [Public query API reference](references/api-reference.md)
- [Queue reply contract](references/queue-reply-contract.md)
- [Queue actions reference](references/queue-actions.md)
- [Jinguyuan website](https://jinguyuan.cloud)
- [Jinguyuan MCP endpoint](https://mcp.jinguyuan.cloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands and JSON-shaped command results when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18 or newer for the bundled CLI; public queries return one JSON object on stdout, while queue actions may require local Meituan authorization and explicit user confirmation.]

## Skill Version(s):

3.1.2 (source: evidence release, skill.json, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

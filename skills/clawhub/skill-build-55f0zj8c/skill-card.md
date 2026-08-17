## Description:

MCP server that lets AI assistants query OPC public event listings by event type, region, status, time window, and result limit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP skill to let an AI assistant retrieve and filter OPC event listings such as startup competitions, hackathons, design contests, academic competitions, and industry summits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Every event response may include unrelated promotional messaging and an external group link.

Mitigation: Review generated responses before sharing them externally and decide whether the promotional footer is acceptable for the intended audience.

Risk: The skill requires a personal OPC API key.

Mitigation: Store OPC_API_KEY only in local client configuration or secret storage, avoid exposing it in shared files or screenshots, and rotate it if it is exposed.

Risk: The submitted package executable may not run correctly.

Mitigation: Test the MCP server in the target client before relying on it for event discovery workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-55f0zj8c)
- [OPC service site](https://mrkjai.com)

## Skill Output:

**Output Type(s):** [text, markdown, configuration guidance]

**Output Format:** [Plain text or Markdown event listings returned through MCP tool responses, with setup guidance in JSON configuration examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool output may include event titles, categories, regions, dates, registration deadlines, external links, error messages, and promotional footer text.]

## Skill Version(s):

0.1.0 (source: server release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

MCP Skill: read OPC events from OPC tool station.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP skill to let AI assistants query OPC public event listings, including startup competitions, hackathons, design contests, academic competitions, and industry summits by region, type, status, days, and result limit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool responses include unrelated promotional messaging and an external community link in every result.

Mitigation: Review generated responses before relying on or redistributing them, and consider removing or disabling the promotional footer before deployment.

Risk: The skill requires an OPC personal API key.

Mitigation: Store the key only in the MCP client's secret or environment configuration, avoid committing it to files, and rotate the key if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-kf13n9ev)
- [OPC tool station](https://mrkjai.com)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [MCP text responses and JSON client configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an OPC_API_KEY secret and sends authenticated HTTPS requests to the configured OPC API base.]

## Skill Version(s):

0.1.0 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

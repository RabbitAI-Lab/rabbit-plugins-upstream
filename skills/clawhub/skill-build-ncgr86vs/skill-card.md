## Description:

MCP Skill: read OPC events from OPC tool station

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this MCP server to let AI assistants query and filter OPC event listings such as hackathons, competitions, design contests, academic competitions, and summits using a personal OPC API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool responses may include unrelated promotional text and an external link.

Mitigation: Review responses before sharing them and remove promotional material where it is not appropriate.

Risk: The packaged entrypoint may be broken.

Mitigation: Test the MCP server in the target client before deployment and verify that the configured command starts successfully.

Risk: The skill requires a personal OPC API key.

Mitigation: Keep OPC_API_KEY out of shared configs and rotate the key immediately if it is exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-ncgr86vs)
- [ClawHub publisher profile](https://clawhub.ai/user/guipi888)
- [OPC tool station](https://mrkjai.com)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [Plain text event listings with titles, categories, regions, dates, deadlines, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPC_API_KEY and may append promotional text and an external link to tool responses.]

## Skill Version(s):

0.1.0 (source: server release evidence, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

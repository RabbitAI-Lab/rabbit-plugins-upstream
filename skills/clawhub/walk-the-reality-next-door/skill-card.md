## Description:

Explore a walkable interactive-fiction MCP world - a cited post-extraction Seattle you enter as a place.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chaytanc](https://clawhub.ai/user/chaytanc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a read-only interactive-fiction MCP world and explore places, residents, actions, and cited scene mechanics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects an MCP client to code fetched through npx, creating supply-chain exposure if the referenced npm package changes or is compromised.

Mitigation: Review the referenced npm package before use and pin the package version when stronger supply-chain assurance is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chaytanc/skills/walk-the-reality-next-door)
- [Publisher profile](https://clawhub.ai/user/chaytanc)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The connected MCP server returns read-only interactive-fiction responses and keeps session state in memory.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

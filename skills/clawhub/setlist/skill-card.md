## Description:

setlist helps agents look up concert setlists and live-music history through setlist.fm using a registered setlist MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music researchers, fans, journalists, and agents use this skill to find artist, venue, tour, date, and city setlist information and to interpret returned live-performance details with source attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses unpinned third-party MCP code that could change between installs.

Mitigation: Pin setlist-mcp to a reviewed package version or commit and prefer a lockfile-backed install.

Risk: The skill requires a setlist.fm API key, which could be exposed if stored in committed project files.

Mitigation: Store SETLIST_API_KEY in a local secret store or uncommitted environment file and avoid printing it in agent outputs.

Risk: Attendance tools can change a user's setlist.fm account state.

Mitigation: Require explicit user confirmation before marking or unmarking concerts as attended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm](https://www.setlist.fm)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include source attribution for setlist.fm results and avoid exposing API keys.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

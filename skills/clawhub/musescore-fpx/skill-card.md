## Description:

Helps agents search MuseScore, inspect score and license metadata, and resolve official download links using a paired browser tab and shell commands without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search MuseScore and inspect score details, licensing, and official download links from a shell without installing a MuseScore MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The browser bridge and its extension access the signed-in browser tab.

Mitigation: Trust @fetchproxy/cli and the Transporter extension before installing, and limit site access to musescore.com.

Risk: Score links may point to content the user is not entitled to download.

Mitigation: Check access rights and use the skill only for content permitted under MuseScore's terms.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/musescore-fpx)
- [MuseScore endpoint reference](references/endpoints.md)
- [MuseScore page-data extraction helper](references/extract-store.js)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Shell commands and JSON score metadata or text download links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Resolves official download URLs but cannot download score files through fpx.]

## Skill Version(s):

1.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

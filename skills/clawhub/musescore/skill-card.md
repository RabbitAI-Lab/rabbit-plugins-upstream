## Description:

Search MuseScore sheet music and read score metadata via MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search MuseScore sheet music, inspect score metadata, and resolve available score downloads or PDFs through a configured MuseScore MCP setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an unreviewed external MCP server and browser extension that mediate requests through the user's signed-in MuseScore browser session.

Mitigation: Install only from trusted sources, review the external server and extension code when possible, and keep the browser extension enabled only while the skill is needed.

Risk: Download and PDF actions can use the signed-in MuseScore session and may access free, entitled, or purchased score content.

Mitigation: Confirm each download or PDF action before allowing an agent to run it, and ensure the requested use complies with MuseScore account permissions and score licensing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musescore)
- [musescore-mcp source repository](https://github.com/chrischall/musescore-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON configuration snippets and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MuseScore search results, score metadata, download URLs, and PDF creation guidance when the external MCP server and browser extension are configured.]

## Skill Version(s):

0.15.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

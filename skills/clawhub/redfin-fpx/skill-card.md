## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search for-sale listings, read property details, inspect market trends and rentals, access climate-risk and photo data, and retrieve signed-in saved homes or saved searches without running the redfin-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation authors, and agents use this skill to compose one-shot fpx shell commands for Redfin real-estate data when the Redfin MCP server is not installed or not desired. It is intended for location resolution, listing search, property detail lookup, market trend inspection, comparable rental checks, climate-risk extraction, photos, and signed-in saved Redfin activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on @fetchproxy/cli and the Transporter browser extension to route requests through a browser session.

Mitigation: Install and use the skill only when those components are trusted, and keep the fpx profile scoped to redfin.com.

Risk: Saved homes and saved searches can expose private real-estate activity from a signed-in Redfin account in shell output.

Mitigation: Run signed-in commands only in trusted terminals and avoid logging or sharing saved-home and saved-search output.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are command-oriented instructions for fpx and jq; Redfin responses may include private saved-home or saved-search data when run through a signed-in browser tab.]

## Skill Version(s):

1.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

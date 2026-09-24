## Description:

tock-fpx helps agents query Tock restaurant discovery, venue availability, and a signed-in user's reservations from shell commands through the fpx CLI and the user's browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to retrieve Tock metros, restaurants, venue calendars, availability, and reservation history without running the Tock MCP server. The skill is read-only and relies on an fpx/Transporter browser session for access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses fpx and the Transporter extension with access to an exploretock.com browser tab.

Mitigation: Install and run it only if that browser-session access is acceptable; keep Chrome site access scoped to exploretock.com and use a signed-in tab only for reservation queries.

Risk: Reservation and profile outputs, including temporary JSON files, may contain names, email addresses, venue details, and booking times.

Mitigation: Treat those outputs as sensitive, avoid sharing them unnecessarily, and remove temporary files after use.

## Reference(s):

- [tock-fpx ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-fpx)
- [Skill instructions](artifact/SKILL.md)
- [Tock request recipes](artifact/references/requests.md)
- [Redux slice extractor](artifact/references/extract-redux-slice.mjs)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown instructions with shell commands, JSON examples, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only workflows; reservation outputs can include personal data from the signed-in Tock account.]

## Skill Version(s):

1.1.2 (source: ClawHub server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

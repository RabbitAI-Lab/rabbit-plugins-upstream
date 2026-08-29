## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search for-sale listings, read property details, market trends, comparable rentals, climate risk, photos, and signed-in saved homes or saved searches through a browser-backed Redfin session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate analysts use this skill to generate fpx shell commands and parsing guidance for Redfin searches, property detail lookups, market data checks, and saved-home workflows without running the Redfin MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-home and saved-search commands can expose private Redfin account preferences, saved locations, and property interests.

Mitigation: Run signed-in commands only intentionally and remove generated files such as /tmp/favs.html or /tmp/page.html when they may contain sensitive data.

Risk: The skill depends on pairing fpx with a Redfin browser tab.

Mitigation: Install only when comfortable with that browser bridge and keep Redfin access scoped to the intended profile.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON parsing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use fpx with a Redfin browser tab and may require signed-in Redfin access for saved homes and saved searches.]

## Skill Version(s):

0.10.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

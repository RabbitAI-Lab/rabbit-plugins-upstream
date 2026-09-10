## Description:

Uses the fpx CLI and a paired Transporter browser tab to query Redfin for location lookup, listings, property details, market trends, rentals, climate risk, photos, and signed-in saved-home data without running the Redfin MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data users use this skill to generate shell commands and guidance for retrieving Redfin listing, property, market, rental, climate, photo, saved-home, and saved-search data through fpx.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-home and saved-search workflows can access private Redfin account data through a signed-in browser session.

Mitigation: Use those endpoints only intentionally, treat returned account data as private, and avoid writing responses to shared temporary files.

Risk: The setup installs @fetchproxy/cli globally and pairs Transporter with redfin.com.

Mitigation: Install only when comfortable with that pairing and consider pinning or verifying @fetchproxy/cli before global installation.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redfin JSON responses may require prefix stripping and resultCode checks; saved-home and saved-search workflows use the user's signed-in Redfin browser session.]

## Skill Version(s):

0.13.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

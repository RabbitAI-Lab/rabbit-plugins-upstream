## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search listings, read property details, inspect market trends, comparable rentals, climate risk, photos, and signed-in saved Redfin data through a browser-backed session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce shell commands and endpoint guidance for retrieving Redfin listing, property, market, rental, climate, photo, saved-home, and saved-search data without running the Redfin MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup installs an unpinned global @fetchproxy/cli package.

Mitigation: Pin and verify the @fetchproxy/cli version before installation.

Risk: A persistent signed-in browser bridge can access private Redfin saved homes and saved searches.

Mitigation: Use a dedicated Redfin browser profile, avoid saved-home and saved-search endpoints unless explicitly needed, and unpair the profile when finished.

Risk: Authenticated Redfin responses may be written to predictable temporary file paths in examples.

Mitigation: Stream authenticated responses when possible or use mktemp with restrictive permissions.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub skill page: redfin-fpx](https://clawhub.ai/chrischall/skills/redfin-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell, jq, sed, and grep snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance focuses on one-shot browser-bridged Redfin requests and response parsing.]

## Skill Version(s):

0.13.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

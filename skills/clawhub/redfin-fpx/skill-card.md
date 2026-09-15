## Description:

Query redfin.com from a shell with the fpx CLI to resolve locations and addresses, search for-sale listings, read property details, market trends, comparable rentals, climate risk, photos, and signed-in saved homes or searches through a browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and real-estate analysts use this skill to ask an agent for Redfin search, listing, property-detail, market-trend, comparable-rental, climate-risk, photo, saved-home, and saved-search queries from shell workflows without running the Redfin MCP server.

### Deployment Geography for Use:

Global; intended for Redfin.com U.S. real-estate data.

## Known Risks and Mitigations:

Risk: Requests route through the user's browser session, which can expose signed-in Redfin data when saved-home or saved-search endpoints are used.

Mitigation: Use the skill only with an intended Redfin session, sign out when saved data is not needed, and review browser extension site access before use.

Risk: The setup documentation uses a global npm installation pattern for fpx.

Mitigation: Prefer a pinned or local fpx install and avoid running npm commands with elevated privileges.

Risk: The examples include temporary-file patterns that could leave Redfin page data in shared locations.

Mitigation: Use private mktemp files or stream outputs directly, and clean up temporary files after use.

Risk: Redfin responses depend on a live browser bridge and may be rejected, capped, or mapped to a substituted service region.

Mitigation: Check bridge health, response resultCode, and serviceRegionName before trusting output in downstream decisions.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/redfin-fpx)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires fpx, the Transporter browser extension, an open redfin.com tab, and Redfin sign-in only for saved-home or saved-search endpoints.]

## Skill Version(s):

0.13.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Query Redfin data from a shell with the fpx CLI, including location resolution, for-sale listings, property details, market trends, comparable rentals, climate risk, photos, and signed-in saved homes or saved searches through a browser-backed Redfin session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Redfin real-estate data in shell scripts or agent workflows without running the Redfin MCP server. It supports property research, listing searches, market checks, rental comparisons, climate-risk lookup, photos, and account-scoped saved homes or searches when the browser tab is signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches may expose private Redfin account data through the user's signed-in browser session.

Mitigation: Ask the agent to access those endpoints only when intended, keep outputs private, and avoid logging or sharing saved-home or saved-search results.

Risk: Requests rely on fpx and the Transporter extension to route Redfin traffic through a browser session, so a paired profile or open signed-in tab can grant access beyond anonymous listing data.

Mitigation: Use a dedicated Redfin fpx profile, confirm the active Redfin tab and sign-in state before requests, and disconnect or unpair when access is no longer needed.

## Reference(s):

- [Redfin stingray endpoints for fpx](references/stingray-endpoints.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands typically use fpx, sed, and jq; Redfin JSON responses require stripping the leading anti-CSRF prefix before parsing.]

## Skill Version(s):

0.13.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

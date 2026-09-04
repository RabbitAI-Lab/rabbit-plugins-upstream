## Description:

Query homes.com from a shell with fpx to search listings, resolve addresses, fetch property details, photos, and history, and read signed-in saved homes or searches through the user's own browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch homes.com listing, property, photo, history, market, and saved-search data through fpx when the homes MCP server is unavailable or unnecessary. It is suited for shell workflows that need homes.com data from the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved homes and saved searches can expose private real-estate preferences or other account-linked browsing data.

Mitigation: Run saved-home and saved-search workflows only on explicit request, and limit extracted outputs to the fields needed for the task.

Risk: The skill depends on a signed-in browser tab and fpx/Transporter pairing, so requests can fail or return sign-in and challenge pages instead of listing data.

Mitigation: Check fpx health, confirm the homes.com tab is signed in and has cleared AWS WAF, and verify response bodies before using extracted data.

Risk: Free-text address resolution may return the closest homes.com result rather than a confirmed match.

Mitigation: Use the documented resolution order and compare the returned candidate address against the requested street address before fetching detail data.

## Reference(s):

- [homes.com request recipes](references/homes-requests.md)
- [homes-fpx ClawHub listing](https://clawhub.ai/chrischall/skills/homes-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Guidance]

**Output Format:** [Markdown with shell commands, JavaScript extraction snippets, jq filters, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce HTML, JSON-LD, JSON, TSV, or parsed listing fields depending on the recipe.]

## Skill Version(s):

1.3.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

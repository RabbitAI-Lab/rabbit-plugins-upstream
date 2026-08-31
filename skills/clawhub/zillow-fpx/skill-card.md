## Description:

Query zillow.com from a shell with the fpx CLI to search listings, fetch property records, price, tax and Zestimate history, photos, market reports, and signed-in saved searches or homes through a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Zillow listing, property, market, photo, and saved-account data with one-shot fpx shell calls when a Zillow MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access personal saved Zillow data through a signed-in browser session.

Mitigation: Ask before fetching saved searches or favorited homes, avoid saving that output unnecessarily, and remove the fpx pairing or profile when persistent access is no longer desired.

Risk: Zillow responses may contain redirects, captcha pages, or bot-wall interstitials even when the fetch command exits successfully.

Mitigation: Check fetched HTML for login redirects, captcha markers, and expected Next.js data before treating results as complete.

## Reference(s):

- [Zillow pages for fpx](artifact/references/pages.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands, jq filters, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reference data fetched through the user's signed-in Zillow browser session.]

## Skill Version(s):

0.12.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

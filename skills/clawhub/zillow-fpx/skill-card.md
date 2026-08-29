## Description:

Query zillow.com from a shell with the fpx CLI to search listings, fetch property records, price and tax history, Zestimate history, photos, market reports, and signed-in saved searches or homes through a user's active Zillow browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data analysts use this skill to guide one-shot Zillow data retrieval from shell scripts without running the Zillow MCP server. It is intended for workflows that need listing search, property details, market data, photos, or a user's own saved Zillow data through an already paired browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved searches, saved homes, and address queries can expose personal Zillow account or real-estate interest data when run through a signed-in browser tab.

Mitigation: Use the saved-data flows only on trusted machines and only when the user intentionally wants to access account-backed Zillow data.

Risk: A successful fpx response can still contain a Zillow login redirect or captcha page instead of the requested data.

Mitigation: Check the fetched HTML for login redirects, captcha markers, and expected __NEXT_DATA__ content before treating an empty or partial result as authoritative.

Risk: The skill depends on Zillow server-rendered page structure rather than a documented public JSON API.

Mitigation: Validate extractor paths against current page output before relying on results in automated workflows.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, Python and jq snippets, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command-oriented guidance; fetched Zillow responses may contain personal saved-search or saved-home data when the browser tab is signed in.]

## Skill Version(s):

0.11.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Query zillow.com from a shell with the fpx CLI to search listings, retrieve property records, history, photos, market reports, and signed-in saved searches or homes through one-shot browser-backed HTTP calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch and parse Zillow listing, property, market, photo, history, and saved-account data from shell workflows when the Zillow MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party browser bridge and globally installed fpx CLI to access Zillow pages.

Mitigation: Pin or verify @fetchproxy/cli before installation and install only when the user is comfortable with that browser-backed access pattern.

Risk: Saved searches and saved homes can expose data from the user's signed-in Zillow account.

Mitigation: Ask the agent to access saved searches or favorites only when the user intends to expose that account data.

Risk: The browser extension may have broader site access than the Zillow workflow requires.

Mitigation: Limit the fetchproxy browser extension's site access to zillow.com.

Risk: Successful fetch commands can still return sign-in redirects or bot-wall pages instead of Zillow data.

Mitigation: Check fetched HTML for login redirects, captcha markers, and expected Next.js page data before trusting parsed results.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions]

**Output Format:** [Markdown with inline shell, Python, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill produces agent guidance for browser-backed Zillow fetches and parsing; it does not directly emit Zillow data without the user running the generated commands.]

## Skill Version(s):

0.13.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

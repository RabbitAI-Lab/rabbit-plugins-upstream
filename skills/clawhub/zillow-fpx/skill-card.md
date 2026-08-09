## Description:

Query zillow.com from a shell with the fpx CLI to search listings, retrieve property records, histories, photos, market reports, and signed-in saved data through a signed-in browser tab without running the Zillow MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to issue shell-based Zillow queries through fpx when they need listing, property, saved-home, saved-search, or market-report data from the user's own browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access privacy-sensitive Zillow account data such as saved searches, favorited homes, and typed addresses through the user's signed-in Zillow tab.

Mitigation: Run saved-data and address commands only when you intend to use the currently signed-in Zillow account, and avoid sharing captured outputs that contain private account or address data.

Risk: A successful fpx command can still return a Zillow login redirect, captcha interstitial, or bot-wall page instead of the expected page data.

Mitigation: Check the fetched HTML for sign-in, captcha, or bot-wall markers before trusting an empty or unusual result.

Risk: The skill depends on Zillow server-rendered page state rather than a documented public API, so page structure changes can break extraction paths.

Mitigation: Treat parsing failures or missing fields as stale extraction guidance and revalidate the page paths before using the result.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell, Python, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that access Zillow through the user's signed-in browser session.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

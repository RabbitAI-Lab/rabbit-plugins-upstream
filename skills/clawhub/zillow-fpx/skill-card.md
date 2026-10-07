## Description:

Helps agents query Zillow listings, property details, market reports, and optionally saved homes and searches through the user's browser session using fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search US Zillow listings and retrieve property, price history, photo, and market information without the Zillow MCP server. With an intentionally signed-in browser tab, they can also retrieve their saved searches and homes.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The browser bridge and fpx can access Zillow pages through the user's browser session.

Mitigation: Install and pair them only if comfortable granting access to zillow.com; review the extension and its site access before use.

Risk: Saved-search and saved-home requests can disclose private Zillow data to the agent.

Mitigation: Use those requests only when intentionally sharing saved data; remove temporary files that contain sensitive addresses.

Risk: A successful fetch may return a sign-in redirect or bot challenge instead of property data.

Mitigation: Check the fetched page for login or challenge markers before using extracted results.

## Reference(s):

- [zillow-fpx ClawHub release](https://clawhub.ai/chrischall/skills/zillow-fpx)
- [Zillow page recipes](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell snippets and JSON extraction examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Property and saved-data results depend on Zillow page availability and the user's browser session.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

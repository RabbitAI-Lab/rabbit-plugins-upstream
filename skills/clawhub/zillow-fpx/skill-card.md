## Description:

Query zillow.com from a shell with the fpx CLI to search listings, retrieve property details, histories, photos, market reports, and signed-in saved searches or homes through a browser-backed session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when they need Zillow property, market, photo, history, or saved-account data from shell workflows without running the Zillow MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved searches, saved homes, and exact-address lookups can expose private account or location information.

Mitigation: Run signed-in examples only when that account data is explicitly needed, and treat returned Zillow data as private.

Risk: A signed-out redirect, login prompt, or captcha interstitial can be returned even when a fetch command exits successfully.

Mitigation: Check fetched HTML for login or bot-wall markers before trusting an empty or partial result.

Risk: The skill depends on Zillow-rendered page structures rather than a documented public JSON API.

Mitigation: Validate extracted fields against current page output before using results in consequential workflows.

## Reference(s):

- [Zillow pages for fpx](artifact/references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON extraction snippets, and jq/Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May depend on a paired fetchproxy browser extension and a signed-in Zillow browser tab for saved searches and saved homes.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

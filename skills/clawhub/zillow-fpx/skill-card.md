## Description:

Zillow FPX helps agents query Zillow pages through the fpx CLI and a signed-in browser tab to search listings, retrieve property records, history, photos, market reports, and saved homes or searches without running the Zillow MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce shell commands, parsing guidance, and setup steps for retrieving Zillow listing, property, market, photo, saved-search, and saved-home data through fetchproxy-backed browser requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved searches and saved homes can expose private Zillow account data when requested through a signed-in browser tab.

Mitigation: Only request or export saved-search and saved-home data when the user intentionally wants that account information used.

Risk: Zillow responses may include sign-in redirects or bot-wall pages even when the transport command succeeds.

Mitigation: Check fetched HTML for login redirects, captcha markers, or missing page data before treating an empty or partial result as authoritative.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, jq, and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include browser-bridge setup steps and JSON extraction paths for Zillow page data.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

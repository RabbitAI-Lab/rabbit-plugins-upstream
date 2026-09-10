## Description:

Query zillow.com from a shell with the fpx CLI to search listings, retrieve property records, price and tax history, photos, market reports, and signed-in saved searches or homes through a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data users use this skill to fetch Zillow listing, property, history, photo, market, and saved-account data from shell workflows when the Zillow MCP server is unavailable or undesired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed-in browser access can expose saved searches, saved homes, exact addresses, and fetched page output.

Mitigation: Treat that data as private, avoid storing it in shared temporary paths or logs, and use a dedicated browser profile when possible.

Risk: The workflow depends on the fetchproxy CLI and browser extension bridging requests through a Zillow tab.

Mitigation: Verify the fetchproxy CLI and browser extension source before installing, and keep browser site access limited to zillow.com.

Risk: Zillow may return login redirects, captcha interstitials, bot-wall responses, or changed page structures while the fetch command still succeeds.

Mitigation: Inspect fetched HTML for redirect, captcha, and bot-wall markers before trusting extracted results.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell, Python, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide users to produce Zillow-derived HTML or JSON output through local fpx calls; fetched saved-search and saved-home data should be treated as private.]

## Skill Version(s):

0.13.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

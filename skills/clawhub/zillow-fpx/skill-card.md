## Description:

zillow-fpx helps agents query Zillow from a shell with the fpx CLI to search listings, retrieve property records, histories, photos, market reports, and signed-in saved Zillow data through a user's browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to draft shell commands and parsing guidance for Zillow listing searches, property lookups, price and tax history extraction, photos, market reports, and saved Zillow data when a direct MCP server is not installed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved-search and saved-home workflows can expose personal Zillow account data through a signed-in browser tab.

Mitigation: Use a dedicated browser profile, limit extension site access to zillow.com, stay signed out unless saved data is needed, avoid unnecessary sensitive addresses, and remove pairing or site access when finished.

Risk: Zillow fetches may return login redirects, captcha pages, or changed page structures while still looking like successful shell calls.

Mitigation: Check fetched HTML for login or captcha markers, run the documented health check, and review parsed results before relying on empty or unexpected output.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, Python, jq, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are operational guidance and commands for use with a user-controlled browser session; the skill itself does not store Zillow credentials.]

## Skill Version(s):

0.13.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

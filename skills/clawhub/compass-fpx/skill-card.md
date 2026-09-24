## Description:

Query Compass real-estate pages from a shell with the fpx CLI to search listings, retrieve property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation operators use this skill to fetch public Compass listing, property, price-history, and agent data from scripts when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fetches run through the user's browser session and depend on the fetchproxy bridge and a Compass tab.

Mitigation: Use a dedicated browser profile when isolation matters, verify the fpx profile before use, and review commands before running them.

Risk: Temporary HTML or JSON files can contain Compass listing or agent data.

Mitigation: Store outputs only as needed and remove temporary files such as /tmp HTML or JSON captures after processing.

Risk: Compass WAF or sign-in interstitials can produce unusable page captures.

Mitigation: Check for documented bot-wall markers and refresh the Compass tab or repair pairing before trusting extracted data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/compass-fpx)
- [Compass request recipes](artifact/references/requests.md)
- [Compass global extraction helper](artifact/references/extract-global.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, jq filters, and JavaScript helper code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use fpx with a Compass browser profile and may write temporary HTML or JSON files for local processing.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

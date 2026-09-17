## Description:

Query compass.com from a shell with the fpx CLI to search listings, retrieve property and agent details, inspect price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data workflows use this skill to query Compass listings, property details, price history, agent listings, and address typeahead results from shell-based FetchProxy calls when the Compass MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FetchProxy reuses a paired browser session for Compass requests.

Mitigation: Use a dedicated browser profile for Compass pairing and confirm the active tab and extension access before running requests.

Risk: The setup installs the fpx CLI globally without a pinned version.

Mitigation: Pin or locally install @fetchproxy/cli when reproducibility or supply-chain controls are required.

Risk: Fetched Compass pages and address queries may contain sensitive search context if written to shared temporary paths.

Mitigation: Avoid shared /tmp paths for fetched pages and clean local HTML or JSON artifacts after use.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, jq snippets, and JSON extraction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces browser-bridged FetchProxy request patterns and extraction commands for Compass pages.]

## Skill Version(s):

0.14.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

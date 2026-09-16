## Description:

Query compass.com from a shell with the fpx CLI to search listings, retrieve property and agent details, read price history, and resolve street addresses through one-shot fetches over a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and real-estate data analysts use this skill to fetch Compass listing, property, agent, price-history, and address-resolution data from shell workflows without running the compass-mcp server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a persistent browser-session bridge through a signed-in Compass browser tab.

Mitigation: Use a dedicated or least-privileged browser profile, keep Chrome site access limited to compass.com, and revoke the fpx pairing when the bridge is no longer needed.

Risk: The setup path installs @fetchproxy/cli globally without a pinned version.

Mitigation: Review or pin @fetchproxy/cli before global installation in managed environments.

## Reference(s):

- [Compass requests for fpx](references/requests.md)
- [extract-global.mjs](references/extract-global.mjs)
- [Compass](https://www.compass.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, JavaScript helper usage, JSON paths, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command recipes and extraction guidance for Compass search, property detail, agent profile, price history, and address typeahead workflows.]

## Skill Version(s):

0.14.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

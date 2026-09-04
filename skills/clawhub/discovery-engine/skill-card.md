## Description:

Discovery helps agents use Disco to upload tabular datasets and return statistically validated, literature-checked patterns with conditions, effect sizes, p-values, citations, novelty classifications, summaries, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and research teams use this skill to run Disco analyses on tabular datasets, identify non-obvious feature interactions or subgroup effects, and present validated findings with supporting citations. It is suited to exploratory pattern discovery when the user has a target column and wants evidence-backed insights rather than manual summary statistics or SQL-style filtering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected tabular datasets are sent to Disco, and public-run data or results may be published.

Mitigation: Confirm public versus private visibility before analysis, avoid sensitive or regulated data unless appropriate private controls are in place, and share only datasets the user is comfortable sending to Disco.

Risk: The skill can guide an agent through account setup, payment methods, subscriptions, and credit purchases.

Mitigation: Require explicit human approval before adding payment methods, buying credits, or changing subscriptions.

Risk: The DISCOVERY_API_KEY grants authenticated access to Disco operations.

Mitigation: Store DISCOVERY_API_KEY as a secret, avoid placing it in prompts or logs, and rotate it if exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco Homepage](https://disco.leap-labs.com)
- [Disco MCP Server](https://disco.leap-labs.com/mcp)
- [Disco API Keys](https://disco.leap-labs.com/developers)
- [Python SDK Reference](artifact/docs/python-sdk.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with structured pattern summaries, report links, JSON-like result fields, code snippets, shell commands, and MCP or SDK configuration examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DISCOVERY_API_KEY for authenticated Disco operations; public analyses may publish data and results, while private analyses consume credits.]

## Skill Version(s):

0.2.171 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

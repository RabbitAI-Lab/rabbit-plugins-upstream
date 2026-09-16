## Description:

Discover and compare suppliers behind brands using Crawlora's ImportYeti company reports and public business websites.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sourcing teams, and business researchers use this skill to build supplier shortlists with observed trade evidence, product fit, official website checks, and open qualification questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supplier research queries, public URLs, extraction schemas, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill for public business research, avoid confidential internal URLs or private sourcing data, and keep the API key scoped in the environment.

Risk: Shipment records may be incomplete, ambiguous, or insufficient to prove manufacturing quality, capacity, willingness to sell, or absence of a trading relationship.

Mitigation: Label shipment data as observed evidence, retain raw ambiguous dates and source URLs, and record unsupported qualification details as unknown.

Risk: Similar company names, subsidiaries, freight forwarders, or trading intermediaries can be mistaken for the intended supplier or brand relationship.

Mitigation: Resolve entities against country, address, official domain, and returned result kind before assigning relationships or using company-report endpoints.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ImportYeti coverage notes](https://www.importyeti.com/our-data)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/supplier-sourcing-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured supplier comparison notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source URLs, collection time, shipment metrics, date scope, and unresolved qualification questions when available.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Discover and compare suppliers behind brands using Crawlora's ImportYeti company reports and public business websites. Use for supplier shortlists, observed sourcing relationships, shipment-activity comparisons, and questions to qualify potential manufacturers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sourcing, procurement, and supply-chain researchers use this skill to discover and compare supplier candidates behind brands using public ImportYeti reports, Bing search, and website extraction. It supports shortlist building, observed trade evidence comparison, fit rationale, and open qualification questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-directed supplier searches and public URLs to Crawlora, which can expose sensitive sourcing intent if used with confidential targets.

Mitigation: Send only supplier research queries and public URLs intended for Crawlora processing, and review Crawlora service terms and data handling before sensitive work.

Risk: The Crawlora API key is a credential required for the helper script.

Mitigation: Keep CRAWLORA_API_KEY in the environment, avoid sharing it in prompts or logs, and use the bundled helper's credential-safe curl behavior.

Risk: Public shipment coverage can be incomplete or ambiguous, so supplier relationships may be missing, duplicated, or misattributed.

Mitigation: Treat shipment data as observed evidence only, preserve source links and raw ambiguous dates, verify entity identity, and avoid treating absence of records as proof of no trade.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ImportYeti coverage notes](https://www.importyeti.com/our-data)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with supplier comparison notes and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supplier findings should preserve source links, collection time, shipment metric scope, fit rationale, and open qualification questions.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

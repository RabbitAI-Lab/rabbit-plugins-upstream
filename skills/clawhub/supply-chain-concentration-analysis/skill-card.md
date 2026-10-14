## Description:

Analyzes observed supplier and origin concentration from Crawlora ImportYeti reports and public company evidence to produce a sourced supply-chain exposure brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and supply-chain analysts use this skill to examine observed importer supplier and origin exposure, compare supported shipment measures, and identify gaps requiring further qualification. The brief is not a procurement audit or guarantee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, requested public URLs, and the API key are sent to Crawlora.

Mitigation: Use the service only if this data sharing is acceptable; keep searches and public-page retrieval limited to the requested companies.

Risk: Incomplete customs records or mismatched periods and measures may overstate supplier or origin concentration.

Mitigation: Verify company identity, report coverage, periods, and denominators; label partial sample shares and avoid treating absent records as zero activity.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/supply-chain-concentration-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown exposure brief with source references, measure ledgers, breakdowns, gaps, and qualification questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observed shipment evidence only; distinguish reporting periods and measures from total procurement.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

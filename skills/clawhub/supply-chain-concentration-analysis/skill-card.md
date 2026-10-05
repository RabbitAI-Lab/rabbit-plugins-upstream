## Description:

Analyzes observed supplier and origin concentration using Crawlora ImportYeti reports and public company evidence to produce a sourced supply-chain exposure brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and supply-chain teams use this skill to examine observed importer, supplier, and origin exposure while preserving shipment measures, time periods, source coverage, and limitations of public customs data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company queries, public URLs, scrape requests, and the API key are sent to Crawlora; confidential procurement details could be exposed if included.

Mitigation: Limit requests to the intended companies and time windows, safeguard the API key, and do not submit private supplier or procurement data without authorization.

Risk: Incomplete public shipment records or mismatched reporting measures can produce misleading concentration estimates.

Mitigation: Identify the measure, period, denominator, and coverage for each estimate; label partial-sample shares and avoid treating them as procurement totals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/supply-chain-concentration-analysis)
- [Crawlora endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown]

**Output Format:** [Markdown exposure brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes entity, period, and measure ledgers; sourced supplier and origin breakdowns; coverage gaps and qualification questions.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

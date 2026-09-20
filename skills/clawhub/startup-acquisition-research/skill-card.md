## Description:

Screen startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen startup acquisition candidates, compare asking prices with dated revenue metrics, inspect revenue history, and turn gaps into diligence questions. It supports research workflows and does not place offers or contact sellers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Acquisition research queries, URLs, and API key usage are sent to Crawlora's API.

Mitigation: Keep CRAWLORA_API_KEY in the environment, use the bounded helper routes only for the diligence task, and avoid submitting unnecessary sensitive information.

Risk: Revenue, MRR, asking price, growth, and deal-score outputs can be mistaken for audited financial facts or investment advice.

Mitigation: Present metrics with dates and definitions, separate payment-provider verification from seller claims and calculations, and treat outputs as research inputs requiring independent diligence.

Risk: Marketplace snapshots, stored records, and daily history can be incomplete, stale, or inconsistent with live details.

Mitigation: Refresh serious candidates with live detail endpoints, record discrepancies, respect missing history, and convert gaps into diligence questions.

## Reference(s):

- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/startup-acquisition-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [TrustMRR FAQ](https://trustmrr.com/faq)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with tables, source links, dated metrics, calculations, discrepancies, and diligence questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API calls through a bounded shell helper and treats marketplace metrics as research inputs, not verified financial advice.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

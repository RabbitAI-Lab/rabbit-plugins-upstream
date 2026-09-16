## Description:

Screen startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history. Use for acquisition candidate shortlists, asking-price comparisons, revenue-history checks, and evidence-based diligence questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and acquisition researchers use this skill to screen public startup acquisition candidates, compare asking prices and dated revenue metrics, and produce evidence-backed diligence questions before deeper review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends acquisition research queries and requested public URLs to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep the API key in the environment, and avoid including secrets or private documents in scrape or search requests.

Risk: Revenue, marketplace, and seller information may be incomplete, unaudited, or stale for acquisition decisions.

Mitigation: Use the skill for public diligence triage and verify revenue, marketplace status, transferability, costs, refunds, retention, and seller claims independently before making financial decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Guidance]

**Output Format:** [Markdown candidate table with source links, dated metrics, explicit calculations, discrepancies, and open diligence questions; may include inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API responses and public URL scraping; financial and marketplace claims should be independently verified before action.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

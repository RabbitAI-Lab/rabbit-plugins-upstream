## Description:

Screen startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Operators, acquisition researchers, and diligence teams use this skill to shortlist startup acquisition candidates, compare asking prices and revenue history, and turn data gaps into follow-up diligence questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Crawlora API key and sends startup slugs, search queries, URLs, and request bodies to Crawlora.

Mitigation: Keep the key in CRAWLORA_API_KEY, limit requests to public pages relevant to the acquisition brief, and avoid putting secrets or confidential deal materials into query strings or scrape bodies.

Risk: Revenue verification, seller asking prices, automated summaries, and deal scores can be mistaken for complete acquisition diligence.

Mitigation: Present those signals separately, preserve dates and metric definitions, and convert gaps around profit, costs, retention, ownership, and transferability into diligence questions.

Risk: Daily revenue_30d history points overlap and can be incorrectly summed as monthly or annual revenue.

Mitigation: Keep metric definitions explicit, do not sum overlapping trailing-30-day points, and label any calculated multiples with their denominator.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/startup-acquisition-research)
- [Crawlora Publisher Profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables, concise prose, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish verified revenue, seller claims, automated summaries, calculations, discrepancies, and open diligence questions.]

## Skill Version(s):

1.0.10 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

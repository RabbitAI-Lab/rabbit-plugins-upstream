## Description:

Compare companies or products using Crawlora website extraction, traffic estimates, reviews, product listings, and hiring data. Use for competitor briefs, positioning and pricing comparisons, or evidence-backed competitive battlecards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketing teams, sales teams, and developers use this skill to produce competitor briefs, pricing and positioning comparisons, and evidence-backed battlecards. It helps separate company claims, third-party observations, and interpretation while preserving source links and uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Competitor names, search queries, target URLs, extraction schemas, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for data you are permitted to send to Crawlora, keep the API key in the environment, and avoid confidential or non-public pages unless appropriate.

Risk: Traffic estimates, reviews, job listings, and discovery rankings can be stale, sampled, low-confidence, or misattributed.

Mitigation: Preserve dates, sample sizes, source URLs, locale settings, and evidence type; verify high-impact claims against primary sources.

Risk: Pricing and positioning data can differ across official pages and third-party sources.

Mitigation: Keep unknowns and disagreements visible instead of averaging incompatible values or treating marketing language as measured performance.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown briefs or comparison matrices with source links, optional shell commands, and JSON observations from Crawlora.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Material claims should include source URLs, source dates, retrieval times, and evidence type.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Signal-Search is an embeddable retrieval skill that routes queries across L0-L3 search depth, scores sources, anchors facts to fetched URLs, and returns concise answers with citations and token-budget controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sabre232](https://clawhub.ai/user/sabre232)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use Signal-Search as a retrieval primitive for fact lookup, research, comparison, source checking, and factual verification. It is best suited to workflows that need concise answers with scored, traceable evidence rather than unranked link lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs live web fetching and includes documented anti-bot evasion techniques.

Mitigation: Review the configured sources, proxies, scraping settings, and compliance controls before installation or production use.

Risk: The skill may use local environment tokens when optional providers or private knowledge-base sources are configured.

Mitigation: Limit environment variables to intended providers, avoid broad credentials, and verify custom source configuration before enabling keyed sources.

Risk: The skill can cache fetched content locally.

Mitigation: Review cache settings and storage locations, especially when queries may touch sensitive or internal information.

## Reference(s):

- [Signal-Search README](README.md)
- [Tier Policy](references/tier-policy.md)
- [Intent Decomposition](references/intent-decomposition.md)
- [Engines](references/engines.md)
- [Anti-Scraping](references/anti-scraping.md)
- [Token Optimization](references/token-optimization.md)
- [Evaluation Golden Set](references/eval-golden-set.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance]

**Output Format:** [Markdown answers or structured JSON with findings, sources, scores, confidence, budget status, tier, and trace.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source citations, confidence signals, token usage, exhaustion status, and exportable citation metadata.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

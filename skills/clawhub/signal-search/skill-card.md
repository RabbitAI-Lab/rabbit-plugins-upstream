## Description:

Signal-Search is an answer-quality search and enhanced-retrieval skill that returns source-scored, fact-anchored, budget-capped answers instead of link lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sabre232](https://clawhub.ai/user/sabre232)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill as an embeddable retrieval primitive for information search, research, comparison, source checking, and fact verification. It is designed to return clean findings with sources, scores, confidence, token use, depth tier, and trace data for the calling agent to evaluate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan classifies the skill as suspicious because it behaves as a broad web-retrieval and scraping library with a credential-aware runtime.

Mitigation: Review before installation and run it only where outbound web requests, system curl execution, optional proxy use, and environment-variable API tokens are acceptable.

Risk: Sensitive tokens or internal source URLs may be exposed if placed in the skill configuration for retrieval use.

Mitigation: Keep compliance controls enabled and avoid adding sensitive tokens or internal URLs unless the deployment explicitly intends the skill to use them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sabre232/skills/signal-search)
- [Server-resolved GitHub provenance](https://github.com/sabre232/signal-search)
- [Anti-scraping and compliance guidance](references/anti-scraping.md)
- [Engine integration specification](references/engines.md)
- [Tier policy L0-L3](references/tier-policy.md)
- [Intent decomposition methodology](references/intent-decomposition.md)
- [Token optimization checklist](references/token-optimization.md)
- [Evaluation golden set](references/eval-golden-set.md)
- [Eastmoney connector example](references/eastmoney-example.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, Guidance]

**Output Format:** [Structured retrieval results with findings, sources, scores, confidence, token usage, exhaustion status, tier, and trace data; may be rendered as Markdown or JSON-like data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses caller-provided LLM, fetch, and bibliography callbacks where needed; token budgets and source policies are configurable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and pyproject.toml report 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

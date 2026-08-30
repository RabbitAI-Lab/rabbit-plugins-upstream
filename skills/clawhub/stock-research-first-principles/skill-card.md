## Description:

Conducts evidence-first stock research with dated sources, data-quality gates, valuation, scenario analysis, falsifiable theses, and research-only recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lee-agi](https://clawhub.ai/user/lee-agi)

### License/Terms of Use:

Apache 2.0

## Use Case:

External users and developers use this skill to produce auditable stock research for single stocks, peer comparisons, sector or theme baskets, and thesis reviews. It helps agents move from dated evidence to valuation, scenario analysis, a falsifiable thesis, and a bounded research stance without trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock research output could be mistaken for personalized financial advice or an instruction to trade.

Mitigation: Treat the skill as a research aid only, independently verify material facts and dates, and do not use its stance as a trade instruction.

Risk: Implicit invocation for stock-analysis prompts may produce output that is not aligned with the user's intended question.

Mitigation: Verify that the response is relevant to the stated research question before relying on the analysis.

Risk: Market and fundamental data may be delayed, incomplete, revised, or wrong.

Mitigation: Require dated sources, retrieval times, evidence-quality checks, and independent verification of material facts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lee-agi/skills/stock-research-first-principles)
- [Data Quality and Provenance](references/data-quality.md)
- [Safety and Communication](references/safety.md)
- [Valuation Standard](references/valuation.md)
- [Research Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Concise Markdown with optional JSON research packets and shell commands for offline planning or validation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research-only output; excludes trade execution, credentials, position sizes, order types, limit prices, and broker payloads.]

## Skill Version(s):

0.1.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

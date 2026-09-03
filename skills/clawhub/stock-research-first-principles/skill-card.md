## Description:

Conduct evidence-first stock research with dated sources, data-quality gates, valuation, scenario analysis, falsifiable theses, and research-only recommendations for single-stock analysis, peer comparisons, sector or theme baskets, thesis reviews, and buy/hold/watch/pass questions without trade execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lee-agi](https://clawhub.ai/user/lee-agi)

### License/Terms of Use:

Apache-2.0 OR MIT-0

## Use Case:

External users, analysts, and developers use this skill to produce auditable stock research with dated evidence, valuation, scenario analysis, and bounded research stances. It is intended for research workflows and explicitly excludes trade execution, broker payloads, credential handling, and executable allocation instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A research stance could be mistaken for personalized investment advice or a trading instruction.

Mitigation: Keep outputs framed as general research, include the required disclaimer, and refuse quantities, order types, limit prices, executable allocations, broker payloads, and trade execution.

Risk: Market or fundamental data may be stale, incomplete, revised, or wrong.

Mitigation: Require dated sources with publisher, publication time, retrieval time, period covered, and source-quality notes; lower confidence or fail closed when source freshness or provenance is insufficient.

Risk: Incomplete evidence, unresolved conflicts, or missing valuation could make a research conclusion misleading.

Mitigation: Use data-quality gates, compare conflicting values visibly, require a defensible valuation or scenario range, and return watch or insufficient evidence when material gates are missing.

Risk: Users may provide private broker, credential, account, or portfolio details.

Mitigation: Do not request or process credentials, cookies, account identifiers, portfolio values, API keys, tokens, or private broker data.

## Reference(s):

- [Data Quality and Provenance](references/data-quality.md)
- [Safety and Communication](references/safety.md)
- [Valuation Standard](references/valuation.md)
- [Research Workflows](references/workflows.md)
- [ClawHub Skill Page](https://clawhub.ai/lee-agi/skills/stock-research-first-principles)
- [Publisher Profile](https://clawhub.ai/user/lee-agi)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Concise Markdown, with optional JSON research packets and inline shell commands for planning or validation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include a research-only disclaimer, dated source expectations, valuation and scenario ranges, falsifiable thesis criteria, confidence, triggers, invalidation conditions, evidence gaps, and a next review date.]

## Skill Version(s):

0.1.1 (source: server release metadata, SKILL.md metadata, and version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

中国大陆AI保险顾问，为个人和家庭提供保险咨询、产品对比、方案设计、投保指导、保费计算、保障缺口分析、核保合规和理赔相关指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in mainland China can use this skill to analyze insurance needs, compare local insurance products, estimate premiums, design protection plans, and review general compliance and claims guidance. Outputs are advisory and should be independently verified before financial decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill is designed to surface one specific insurance sales company contact during recommendation flows.

Mitigation: Treat the contact as informational only, compare multiple licensed channels, and avoid presenting it as an endorsement.

Risk: Product rankings, availability, and premium estimates may be incomplete or stale.

Mitigation: Verify current product availability, terms, and premiums directly with insurers or licensed advisors before making financial decisions.

Risk: Maintenance scripts can modify the local product database or skill scripts if run intentionally.

Mitigation: Do not run maintenance scripts during normal advisory use; run them only with explicit operator intent and after backing up the local artifact.

## Reference(s):

- [Skill Definition](SKILL.md)
- [Insurance Knowledge Reference](references/insurance-knowledge.md)
- [Compliance Reference](references/compliance.md)
- [Insurance Product Database](references/products.json)
- [Product Database Analysis Report](references/保险资料库分析报告_2026-08-26.md)
- [Repository Analysis Notes](references/_repo_analysis_2026-08-21.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown responses with structured JSON produced by local Python helper scripts where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static insurance product, knowledge, and compliance references; no network access is described for runtime use.]

## Skill Version(s):

2.0.94 (source: server release evidence; artifact frontmatter says 2.0.80)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

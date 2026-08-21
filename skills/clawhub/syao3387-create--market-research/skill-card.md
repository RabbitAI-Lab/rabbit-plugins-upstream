## Description:

Market Research Agent guides an agent through structured market, product, competitor, user, brand, and marketing analysis using a nine-module Signal-Insight-Opportunity-Action framework.

This skill is ready for commercial/non-commercial use.

## Publisher:

[syao3387-create](https://clawhub.ai/user/syao3387-create)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market, product, brand, or marketing teams use this skill to generate Chinese-language research reports for categories, products, competitors, and customer segments. It structures findings into traceable signals, insights, opportunities, and actions for U.S.-market decision-making.

### Deployment Geography for Use:

United States focus for analysis; global deployment review recommended.

## Known Risks and Mitigations:

Risk: The skill defaults to Chinese-language reports and a U.S.-market perspective, which may produce mismatched assumptions for other regions or languages.

Mitigation: Explicitly specify the desired market, language, and target user profile, then verify regional assumptions before relying on the report.

Risk: Market research outputs can be misleading if data sources are missing, stale, or weak.

Mitigation: Require traceable sources for signals and preserve the skill's data-gap labeling instead of treating unsupported conclusions as facts.

## Reference(s):

- [Market Research Structured Analysis Framework](references/framework.md)
- [Market Research Agent on ClawHub](https://clawhub.ai/syao3387-create/skills/market-research)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language Markdown report with tables and structured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to a U.S.-market perspective and includes a research method section; data gaps are labeled rather than filled speculatively.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

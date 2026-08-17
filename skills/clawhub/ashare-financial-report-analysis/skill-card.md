## Description:

A股上市公司财报结构化拆解系统。基于16节固定模板，对季报/年报进行一手数据提取、自算核验、跨季度可比的结构化分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and analysts use this skill to generate structured A-share quarterly and annual report analyses from public market data sources. It helps compare companies and periods through a fixed 16-section report, source citations, and self-calculated financial checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial-report outputs may be mistaken for investment advice or trading recommendations.

Mitigation: Review the cited data sources and treat valuation or trading implications as analysis rather than investment advice, as directed by the security guidance and artifact disclaimer.

Risk: Public market data APIs may return missing, delayed, permission-limited, or inconsistent values.

Mitigation: Use the skill's source priority and cross-check rules, mark unavailable fields explicitly, and self-calculate key metrics such as FCF before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenxyzcyxpp/skills/ashare-financial-report-analysis)
- [README](artifact/README.md)
- [README.en](artifact/README.en.md)
- [A-share earnings template](artifact/references/a-share-earnings-template.md)
- [Tengjing 2025 case study](artifact/references/case-study-tengjing-2025.md)
- [CNINFO](http://www.cninfo.com.cn)

## Skill Output:

**Output Type(s):** [markdown, analysis, API calls, guidance]

**Output Format:** [Markdown structured financial-report analysis with tables, formulas, source notes, and risk flags]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a fixed 16-section A-share earnings report and marks missing or unavailable financial data instead of fabricating values.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

This skill helps CECEP Valiant market staff pre-screen customer inquiries through information checks, product classification, five-factor scoring, and R&D cost estimates, then produce a visual HTML analysis form.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Market department users at CECEP Valiant use this skill after receiving customer inquiry emails to decide whether to quote directly, escalate to a supervisor, push the request to R&D, or send a polite rejection. It supports a repeatable desktop screening process before R&D investment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer inquiry details and internal product information may be sensitive.

Mitigation: Review what data is entered into the workflow and limit access to authorized market, supervisor, and R&D staff.

Risk: Configured Zhihuiya MCP or database access could expose data beyond the intended screening task.

Mitigation: Review the MCP account authorization, database scope, and access permissions before enabling real-time lookup.

Risk: Manual scoring can produce misleading recommendations when inquiry details, product records, or cost estimates are incomplete.

Mitigation: Require missing-field checks, supervisor review for borderline scores, and R&D confirmation before committing to new development work.

## Reference(s):

- [Inquiry Pre-Screening Method](artifact/references/01_screening_method.md)
- [Market Analysis HTML Template](artifact/references/market_analysis_template.html)
- [Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [CECEP Valiant](http://www.valiant-cn.com/cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance plus a local HTML analysis form and generated business text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces five-factor scoring, R&D push-form content, print/PDF-ready HTML, and polite rejection text; database-backed conclusions require configured Zhihuiya MCP access.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

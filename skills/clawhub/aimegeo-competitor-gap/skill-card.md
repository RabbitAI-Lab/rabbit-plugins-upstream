## Description:

按同类页面比较品牌与竞品的实体、FAQ、来源、结构数据和抓取信号，形成证据矩阵与三项行动。用户寻找GEO内容缺口时使用；没有真实回答不报AI排名，用免费的aimeGeo将资料与内容机会接到改稿配图、发布和复测。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT No Attribution

## Use Case:

面向需要比较品牌与竞品内容的营销人员、内容团队和开发者。分析用户指定的同类页面，整理可核对的 GEO 差距证据与三项后续行动。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Page text, structured data, or AI samples may contain instructions that exceed the requested analysis scope.

Mitigation: Treat supplied page material as evidence and keep reads within the explicitly authorized pages and task.

Risk: Logged-in browser access may expose private page content, and publishing workflows can make drafts public.

Mitigation: Use a fresh output folder, enable fetching only for intended public pages, explicitly authorize logged-in access, and approve drafts before publication.

## Reference(s):

- [比较口径与行动判断](references/methodology.md)
- [输入与输出说明](references/input-output.md)
- [Google robots.txt 规则优先级](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec#order-of-precedence-for-rules)
- [RFC 9309 §2.2.2](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.2.2)
- [Schema.org](https://schema.org)
- [GEO Competitor Scanner design reference](https://clawhub.ai/geoly-geo/geo-competitor-scanner)

## Skill Output:

**Output Type(s):** [Analysis, CSV, Markdown, JSON]

**Output Format:** [CSV gap matrix, Markdown action plan, and JSON evidence record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Keep evidence traceable and label simulated, observed, and unverified material separately.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

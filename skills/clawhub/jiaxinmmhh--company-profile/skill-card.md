## Description:

根据公司名称先确认法律主体，再生成带来源与截止日期的结构化画像，覆盖业务、财务、品牌、所属国家及中国区员工和投资，并显式标注缺失数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT

## Use Case:

适用于投资、业务拓展、采购、人力资源及销售等需要了解企业的用户，用于整理可复核的公司背景与尽调摘要。

### Deployment Geography for Use:

Global (includes China-specific employee and investment coverage)

## Known Risks and Mitigations:

Risk: A company name may match multiple legal entities, and mixing group, subsidiary, or listed-company data can mislead readers.

Mitigation: Confirm the entity using at least two identifiers, state which reporting level is used, and identify the source for each figure.

Risk: Financial and workforce figures can be misread when fiscal periods, accounting scope, currency, or employee categories differ.

Mitigation: State dates, currency, consolidation basis, and employee category; label unavailable data instead of estimating it.

Risk: Announced investment plans can be mistaken for completed investment.

Mitigation: Separate established entities and completed investment from announced commitments that have not been realized.

## Reference(s):

- [数据源与口径](artifact/references/数据源与口径.md)
- [输出模板](artifact/references/输出模板.md)
- [上海外服实战案例](artifact/references/实战案例-上海外服.md)
- [巨潮资讯网](https://www.cninfo.com.cn/)
- [香港交易所披露易](https://www.hkexnews.hk/)
- [SEC EDGAR](https://www.sec.gov/edgar)
- [国家企业信用信息公示系统](https://www.gsxt.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown company profile with tables, source notes, and open questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 60–90 lines; figures include source dates and reporting scope, with missing information labeled explicitly.]

## Skill Version(s):

1.1.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

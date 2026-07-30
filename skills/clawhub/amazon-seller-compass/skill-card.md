## Description: <br>
Amazon 卖家指南针 helps experienced Amazon sellers evaluate product and category opportunities through market scanning, competitor analysis, FBA profit modeling, keyword research, and decision-ready Markdown reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shylamb-token](https://clawhub.ai/user/shylamb-token) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce operators use this skill to research product categories or specific ASINs, compare competitors, estimate FBA profitability, identify keyword opportunities, and generate a local Markdown decision report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on public web research for Amazon, FBA fee, competitor, and keyword data that can be incomplete or change quickly. <br>
Mitigation: Require current source citations, verify important fee and demand assumptions, and treat unsupported values as estimates before making commercial decisions. <br>
Risk: Local Markdown reports may include private Seller Central data, credentials, supplier terms, or other confidential business inputs if the user provides them. <br>
Mitigation: Avoid providing credentials or confidential data, confirm the output path before writing when needed, and redact sensitive details before sharing reports. <br>


## Reference(s): <br>
- [Data Sources and Search Strategy](references/data-sources.md) <br>
- [Amazon FBA Fee Structure and Profit Calculation Reference](references/fba-fees.md) <br>
- [Product Selection Decision Report Template](references/report-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/shylamb-token/skills/amazon-seller-compass) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown report saved to a local file, plus a concise chat summary and decision rating] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include source-labeled market data, competitor tables, FBA profit models, keyword opportunities, risks, and next actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

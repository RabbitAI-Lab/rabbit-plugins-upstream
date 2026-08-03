## Description: <br>
在决定参与 Alibaba RFQ 后，按平台字段生成并检查产品、价格、数量、交期、贸易条款、保修和买家留言。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales or sourcing operators use this skill after deciding to participate in an Alibaba RFQ to prepare platform-ready quote fields, buyer-facing message text, and submission readiness checks. It helps identify missing, conflicting, or unverified quote inputs before a human manually submits anything. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unverified RFQ details could lead to inaccurate quote text. <br>
Mitigation: Verify prices, inventory, trade terms, warranty, and buyer messages before manually submitting anything on Alibaba. <br>
Risk: Missing or conflicting product, quantity, currency, condition, lead time, trade term, validity, or warranty inputs could make the quote unsuitable for submission. <br>
Mitigation: Use the parameter status table and stop conditions; resolve missing or conflicting inputs before generating submit-ready fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-ali-rfq-bid) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with parameter status tables, Alibaba RFQ field drafts, buyer message text, risk notes, and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only output; no automatic Alibaba submission, tool calls, shell commands, or hidden execution behavior.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata); artifact documentation reports internal draft v0.2.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

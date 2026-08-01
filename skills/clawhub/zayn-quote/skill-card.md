## Description: <br>
在报价发出前检查型号、数量、价格、成色、库存、交期、贸易条款、付款和保修是否完整一致。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and quotation users use this skill to review business quote details before sending, including model, quantity, price, condition, inventory, delivery timing, trade terms, payment, and warranty. It helps identify missing, conflicting, or unverified quote fields and produces a structured readiness review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Quote review output may be mistaken for confirmation of price, inventory, delivery, warranty, or trade terms. <br>
Mitigation: Verify those business facts with normal business sources before sending a quote. <br>
Risk: Missing or conflicting quote fields can lead to an unsafe send-ready conclusion. <br>
Mitigation: Use the skill's required parameter status table and do not treat a quote as send-ready when price, condition, inventory, delivery timing, or trade terms are missing or unresolved. <br>
Risk: Draft artifact notes indicate real anonymized test cases are still pending. <br>
Mitigation: Review outputs against representative quote cases before relying on the skill in a production workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-quote) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured review sections and parameter status tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reviews user-provided quote facts; does not confirm price, inventory, delivery, warranty, or trade terms independently.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

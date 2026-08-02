## Description: <br>
综合采购报价、客户价值、数量、成色、交期、付款和风险，制定报价策略和可谈边界。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, procurement, and quotation teams use this Chinese-language skill to assess quotation strategy from customer needs, purchase cost basis, quantity, delivery, payment, and risk context. It helps structure pricing rationale, negotiation boundaries, and items requiring human confirmation without automatically setting a final sale price. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may enter sensitive business pricing, customer, payment, or supplier context while using the skill. <br>
Mitigation: Provide only the minimum necessary or de-identified commercial context in the agent environment, and review any generated guidance before sharing it outside the authorized team. <br>
Risk: Incomplete or conflicting inputs could lead to misleading quotation strategy or false precision. <br>
Mitigation: Use the skill's parameter status table and minimum operating conditions; keep outputs preliminary until missing, conflicting, or unverified facts are resolved by a human. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-price) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown with a parameter status table and structured quotation strategy sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include pricing rationale, risk factors, negotiation space, suggested quote structure, and human-confirmation items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact docs mention v0.1 draft status) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

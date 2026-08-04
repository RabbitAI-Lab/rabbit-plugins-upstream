## Description: <br>
根据客户状态、上次沟通、时间节点和可补充价值，判断是否跟进、何时跟进以及跟进什么。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and customer-facing users use this skill to decide whether a customer follow-up is justified, when to follow up, what value to add, and when to pause outreach. It helps structure follow-up decisions without automating messages or replacing human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer records may contain sensitive sales history or communication details. <br>
Mitigation: Review and minimize customer data before sharing it with the agent. <br>
Risk: The skill may produce advisory follow-up recommendations that affect customer contact, pricing, inventory, payment, or compliance decisions. <br>
Mitigation: Require human approval before acting on recommendations or sending customer-facing messages. <br>
Risk: The artifact describes the protocol as draft and not yet validated with real customer follow-up cases. <br>
Mitigation: Use outputs as a checklist, validate against real or de-identified cases, and keep stop conditions in place. <br>
Risk: Weak behavior signals such as website views or email opens can be overread as purchase intent. <br>
Mitigation: Keep evidence strength explicit and avoid escalating follow-up priority without stronger customer, order, inquiry, or value signals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-followup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown advisory checklist with tables and suggested follow-up wording when conditions are met] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review for customer facts, evidence strength, outreach timing, and any pricing, inventory, payment, compliance, or customer-contact decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documents v0.2.0 draft protocol) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

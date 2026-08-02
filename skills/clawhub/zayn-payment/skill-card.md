## Description: <br>
根据付款条款、约定日期、财务到账状态和客户承诺，判断是否提醒、如何提醒以及何时升级。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams handling order, delivery, and payment follow-up use this skill to classify payment status, decide whether to send reminders, draft customer-facing follow-up text, and identify when escalation or internal action is needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment guidance may be wrong if finance status, due dates, amounts, or customer commitments are incomplete or stale. <br>
Mitigation: Verify finance records, payment amounts, and customer commitments before using the recommendation or sending customer-facing text. <br>
Risk: Outputs could imply shipment, delivery, or continued execution before internal authorization is confirmed. <br>
Mitigation: Treat the skill as guidance only and require human review before promising shipment, delivery, or continued execution. <br>
Risk: Customer-facing reminders can create relationship or compliance risk if they use accusatory language or expose internal cash-flow concerns. <br>
Mitigation: Review sendable messages manually and keep language factual, neutral, and limited to verified payment and order information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-payment) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured sections and optional customer-facing message text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided payment terms, due date, finance status, customer commitment, and communication goal before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Generates channel- and language-appropriate customer replies from the customer's original message, confirmed facts, reply goals, and commitment boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, support, and account-management users use this skill to check whether a customer reply has enough confirmed facts and clear boundaries before drafting. It helps produce concise Email, WhatsApp, WeChat, LinkedIn, or similar customer-facing replies while avoiding premature commitments and unsupported claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A generated customer reply could treat unconfirmed prices, inventory, delivery timing, warranty terms, or responsibility as facts. <br>
Mitigation: Require confirmed facts and commitment boundaries before producing send-ready wording, and stop or request internal confirmation when key inputs are missing or conflicting. <br>
Risk: Draft wording could expose internal procurement, engineering, supplier, or management issues to a customer. <br>
Mitigation: Review the draft for internal-only details and rewrite customer-facing language around confirmed facts, safe boundaries, and the next external action. <br>
Risk: The skill may produce wording that fits US business English but not the user's target locale or channel. <br>
Mitigation: Provide the desired language, channel, tone, and locale expectations, then review the output before sending. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-reply) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured analysis tables and draft reply text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stop before generating a send-ready reply when required facts, goals, or commitment boundaries are missing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation describes draft protocol version 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

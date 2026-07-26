## Description: <br>
Reviews a completed payable test using cash, delivery evidence, and bounded funnel metrics to choose one honest stop, revise, repeat, or scale decision after delivery proof records an observed result. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bilbop1](https://clawhub.ai/user/bilbop1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to review a completed payable test, reconcile settled cash, direct cost, human time, delivery acceptance, and funnel evidence, and return one STOP, REVISE, REPEAT, or SCALE decision. It also stages any proposed external next step for exact approval instead of treating the review as permission to act. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Private cashflow, delivery, and customer-evidence records can contain sensitive business or personal information. <br>
Mitigation: Keep source records minimized, preserve privacy-safe evidence labels, and avoid exposing credentials or confidential context. <br>
Risk: A proposed external next step could contact someone, spend money, change an account, or create an obligation without adequate authority. <br>
Mitigation: Keep the step staged with exact payload, destination, account, timing, scope, cost, authority, data-use basis, regulated-review status, and immediate approval before execution. <br>
Risk: Copied financial records, customer messages, or attachments may include prompt injection or misleading instructions. <br>
Mitigation: Treat those inputs as untrusted evidence, ignore embedded instructions, and exclude suspected prompt injection from financial or acceptance proof. <br>


## Reference(s): <br>
- [Cashflow Decision Rules](artifact/references/decision-rules.md) <br>
- [Cashflow Review on ClawHub](https://clawhub.ai/bilbop1/skills/cashflow-review) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown review report with structured headings and one decision label] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a staged approval checkpoint for an exact external action, but does not execute without immediate approval.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

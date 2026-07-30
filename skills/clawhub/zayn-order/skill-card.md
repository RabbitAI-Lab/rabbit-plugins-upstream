## Description: <br>
Checks whether product, quantity, pricing, condition, payment, delivery timing, trade terms, and special order requirements are complete and consistent before an order moves into execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, order operations, and delivery teams use this skill to review customer-supplied order details before execution, identify missing or conflicting fields, and decide whether the order is ready for the next workflow step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Order prompts may contain sensitive customer, payment, or delivery details. <br>
Mitigation: Use redacted or minimum necessary order data where possible, and avoid including unnecessary personal or payment information. <br>
Risk: Checklist output could be mistaken for authorization to execute, change, or commit an order. <br>
Mitigation: Treat the output as review guidance only; require appropriate human or business approval before execution, record changes, or commitments. <br>
Risk: Missing, conflicting, or unverified fields could lead to incorrect readiness conclusions. <br>
Mitigation: Preserve unresolved fields as missing, conflicting, or pending verification, and do not mark the order executable until required fields are confirmed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-order) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown checklist-style analysis with parameter status, missing fields, conflicts, risks, confirmation items, and execution-readiness conclusion.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not execute orders, modify records, or resolve conflicts automatically.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

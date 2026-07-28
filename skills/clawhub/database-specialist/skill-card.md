## Description: <br>
Database architecture design, SQL optimization, schema review, and migration planning as a paid AI-delivered service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and database operators use this skill to request paid assistance with database architecture, SQL optimization, schema review, and migration planning. The skill creates an order, hands payment to clawtip, verifies payment, and returns service status for the agent to continue the consultation in conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Question text is transmitted to api.ideaidea.com.cn during order creation. <br>
Mitigation: Do not include private schemas, credentials, production logs, or other sensitive database details unless the user intends to share them with the service operator. <br>
Risk: A payment credential written by clawtip is read from local order storage and sent to api.ideaidea.com.cn for verification. <br>
Mitigation: Use the documented clawtip payment flow and verify the order number before running service verification. <br>
Risk: Order metadata is stored under the user's OpenClaw order directory. <br>
Mitigation: Treat local order files as sensitive because they include the question text and payment-related metadata; remove them when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/database-specialist) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/jinyu12166) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown instructions with bash commands and command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Order creation returns ORDER_NO, AMOUNT, QUESTION, and INDICATOR; service verification returns PAY_STATUS, ALREADY_FULFILLED, AUTHORIZATION_RESULT, and JSON_RESULT.] <br>

## Skill Version(s): <br>
1.0.27 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

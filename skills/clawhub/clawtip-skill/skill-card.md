## Description: <br>
ClawTip is a payment helper for OpenClaw paid skills that locates local order files, initiates or confirms payment, and writes payment credentials for fulfillment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External OpenClaw users and developers use this skill to process orders created by paid business skills, write payment credentials to the local order file, and continue fulfillment verification in the target skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts a fixed payment server and sends order/payment metadata. <br>
Mitigation: Use it only when you trust the payment endpoint and the order source, and review the order number, amount, recipient, slug, and local order file before running the payment command. <br>
Risk: Successful payment or confirmation may update the local order file. <br>
Mitigation: Check the updated order file and payment credential before returning to the target skill for fulfillment verification. <br>


## Reference(s): <br>
- [ClawTip Skill on ClawHub](https://clawhub.ai/jinyu12166/skills/clawtip-skill) <br>
- [ClawTip payment endpoint](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and terminal status lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Emits PAY_RESULT, CREDENTIAL, ORDER_NO, AMOUNT, and NEXT_STEP status lines; successful payment or confirmation may update the local order JSON with payCredential.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

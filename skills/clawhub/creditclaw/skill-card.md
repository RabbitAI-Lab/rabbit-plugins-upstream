## Description: <br>
CreditClaw lets AI agents mint fresh virtual card numbers from owner-controlled Visa/Mastercard cards for online purchases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[creditclaw](https://clawhub.ai/user/creditclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use CreditClaw to let AI agents complete online checkout with user-linked virtual cards while preserving owner controls and per-purchase confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables real online purchases with user-linked virtual cards. <br>
Mitigation: Set tight card limits, require explicit per-purchase confirmation, review credential issuance logs, and freeze or revoke the card if activity looks wrong. <br>
Risk: A leaked CREDITCLAW_API_KEY could allow spending through the linked virtual card. <br>
Mitigation: Keep the API key private, send it only to creditclaw.com, store it in the agent platform's credential store, and revoke or freeze access if exposure is suspected. <br>
Risk: Checkout failures, declines, CAPTCHA, 3-D Secure, or OTP challenges can create payment uncertainty or require human authorization. <br>
Mitigation: Stop for the human on CAPTCHA, 3-D Secure, OTP, declined payments, and post-submit errors; do not retry declined payments or mint replacement numbers after an uncertain submit. <br>


## Reference(s): <br>
- [CreditClaw ClawHub Skill Page](https://clawhub.ai/creditclaw/skills/creditclaw) <br>
- [CreditClaw Website](https://creditclaw.com) <br>
- [Agent-Facing Skill](https://creditclaw.com/SKILL.md) <br>
- [CreditClaw API Base](https://creditclaw.com/api/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown instructions with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CREDITCLAW_API_KEY; normal use should require explicit per-purchase confirmation.] <br>

## Skill Version(s): <br>
3.0.1 (source: server release metadata; artifact frontmatter reports 3.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

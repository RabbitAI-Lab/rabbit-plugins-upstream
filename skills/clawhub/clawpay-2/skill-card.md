## Description: <br>
Private payments for AI agents - no on-chain link between sender and recipient <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mmchougule](https://clawhub.ai/user/mmchougule) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to prepare private USDT payment flows through the ClawPay API, including invoice creation, signed transfer requests, status checks, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to handle a wallet private key and perform real blockchain transfers. <br>
Mitigation: Use a dedicated wallet with minimal funds, avoid hardcoding valuable private keys, and verify each recipient and amount before execution. <br>
Risk: Payment execution depends on trusting clawpay.dev, signed messages, and on-chain transfer behavior. <br>
Mitigation: Review the skill carefully before installation and use it only when the operator understands what the signatures and transfers authorize. <br>


## Reference(s): <br>
- [Clawpay Skill Page](https://clawhub.ai/mmchougule/skills/clawpay-2) <br>
- [ClawPay API](https://clawpay.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JavaScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes wallet configuration, API endpoint examples, and payment troubleshooting guidance.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

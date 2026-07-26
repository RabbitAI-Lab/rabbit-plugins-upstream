## Description: <br>
Zhifubao guides developers through Alipay Open Platform integration, including payment-product selection, sandbox testing, RSA2 signing, async notification verification, and common error triage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and troubleshoot Alipay payment integrations, including product selection, sandbox validation, signing, callback verification, and payment error triage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Alipay product terms, fees, and API behavior may differ from the skill's guidance. <br>
Mitigation: Verify current product terms, pricing, and API details in official Alipay documentation before production use. <br>
Risk: Private keys or production credentials could be exposed if shared while troubleshooting payment integration issues. <br>
Mitigation: Keep private keys and production credentials out of chats and logs, and redact secrets from any examples. <br>
Risk: Incorrect callback handling can cause duplicate or incorrect payment state updates. <br>
Mitigation: Use signature verification, amount checks, idempotent order updates, and reconciliation before enabling production payment flows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhangifonly/skills/zhifubao) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zhangifonly) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration, code] <br>
**Output Format:** [Markdown prose with checklists, tables, and inline code identifiers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only; no automatic API calls, credential collection, or financial actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

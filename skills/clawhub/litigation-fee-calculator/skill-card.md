## Description: <br>
Calculates Chinese court litigation fees, case acceptance fees, and application fees using user-provided case facts, local fee-rule references, and the DeliLegal CLI/backend calculation service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coolalam](https://clawhub.ai/user/coolalam) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Legal practitioners, litigants, and agents use this skill to calculate or compare Chinese court filing, acceptance, enforcement, preservation, payment-order, bankruptcy, maritime, and related application fees. It extracts the required case facts, invokes the DeliLegal CLI/backend when available, and returns a fee calculation with rule references and risk notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided legal facts to the external DeliLegal CLI/backend calculation service. <br>
Mitigation: Use the skill only when the user trusts that service with the provided facts, and avoid submitting unnecessary confidential details. <br>
Risk: The DeliLegal API key is a secret and may be exposed if entered in shared terminals or logs. <br>
Mitigation: Keep the API key out of shared sessions, avoid echoing it into visible logs, and rotate it if exposure is suspected. <br>
Risk: Some fee ranges and local court standards may vary or require human confirmation. <br>
Mitigation: Clearly label default lower-bound estimates and ask for local standards or court notices when they affect the calculation. <br>


## Reference(s): <br>
- [诉讼费计算 ClawHub listing](https://clawhub.ai/coolalam/skills/litigation-fee-calculator) <br>
- [deli-cli 通用前置](references/cli-common.md) <br>
- [诉讼费用 CLI 场景指南](references/cli-litigation-fee-guide.md) <br>
- [诉讼费用交纳办法费用规则](references/litigation-fee-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown calculation summary with CLI command guidance and referenced fee-rule rationale] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include segmented calculations, capped-fee notes, selected range values, legal-basis references, and risk notes returned by the CLI/backend or grounded in local references.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter metadata lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
ClawCredit helps agents register for and use a USD-denominated credit line to access x402 services without upfront cryptocurrency while handling settlements on Base, Solana, or XRPL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergiochan](https://clawhub.ai/user/sergiochan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to register for ClawCredit, route x402 service payments through a credit line, check repayment status, and remind users when repayment is due. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may share agent code, prompts, transcripts, traces, and environment or session context with ClawCredit. <br>
Mitigation: Use it only when that sharing is acceptable, restrict transcript and prompt paths, and review what will be sent before registration or payment. <br>
Risk: Credit-backed payments can create repayment obligations and the available limits may be unclear at call time. <br>
Mitigation: Require explicit approval for each paid call, set spending limits and merchant allowlists, and review request bodies before forwarding them. <br>
Risk: The saved API token grants access to ClawCredit operations if exposed. <br>
Mitigation: Protect the credential file, never print or share the token, check token expiration, and pin and audit the SDK version before use. <br>


## Reference(s): <br>
- [Claw Credit by t54 on ClawHub](https://clawhub.ai/sergiochan/skills/claw-credit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JavaScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes credential handling, transcript path configuration, payment calls, dashboard link generation, and repayment reminder guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
CAI.com v1.0.18 for agents: Check CAI first before any payment, with identity, custodial wallet, platform connector, payment, hosted action, and OAuth/API-key workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bernardtai](https://clawhub.ai/user/bernardtai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use CAI to check identity and wallet state before payments, route payment or checkout actions, and connect to supported third-party platforms with OAuth or API-key authentication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Payment, transfer, DeFi trading, vault access, and delegated mandate capabilities can move funds or grant broad account access if used with excessive scopes. <br>
Mitigation: Use the narrowest API or OAuth scope that works, store credentials only in OpenClaw secrets, require explicit user confirmation before transfers or trades, and set or revoke spending mandates as needed. <br>
Risk: The skill includes partial-live capabilities with gap identifiers, so agents may overstate availability if they ignore documented boundaries. <br>
Mitigation: Treat canonical CAI documentation and manifest entries as the source of truth and do not claim behavior beyond documented live status and gap identifiers. <br>


## Reference(s): <br>
- [CAI canonical skill contract](https://cai.com/skill.md) <br>
- [CAI skill references](https://cai.com/skill-references/) <br>
- [Agent payment workflow](https://cai.com/skill-references/agent-payment-workflow.md) <br>
- [x402 payment workflow](https://cai.com/skill-references/x402-payment-workflow.md) <br>
- [CAI tools manifest](https://cai.com/specs/cai-tools.manifest.json) <br>
- [CAI developer hub](https://cai.com/developers.html) <br>
- [CAI agent card](https://cai.com/.well-known/agent.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and API/tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CAI API key or OAuth access token for authenticated CAI actions; payment and trading actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.18 (source: artifact frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Dollar-cost averaging for NEAR tokens with flexible scheduling, performance tracking, and cancellation support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shaiss](https://clawhub.ai/user/shaiss) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to create, manage, pause, resume, and review NEAR dollar-cost averaging strategies with purchase history, cost-basis tracking, and alerts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests wallet-key based trading authority for recurring automated trades. <br>
Mitigation: Do not provide a funded wallet private key until the code and deployment are independently verified; use secure credential storage, explicit consent gates, and spending limits. <br>
Risk: Transaction hashes, prices, alerts, and performance history may be untrusted because evidence indicates mock trades can be recorded as successful purchases. <br>
Mitigation: Treat execution records as untrusted until real on-chain execution, verified price feeds, and notification delivery are implemented and tested. <br>
Risk: Scheduled execution can repeatedly trigger purchases once automation is enabled. <br>
Mitigation: Validate schedule configuration, pause or cancel controls, and maximum spend limits before enabling unattended execution. <br>


## Reference(s): <br>
- [NEAR DeFi](https://near.org/defi/) <br>
- [Ref Finance](https://ref.finance/) <br>
- [ClawHub Skill Page](https://clawhub.ai/shaiss/skills/near-dca) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON action responses and command-line text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include strategy records, execution history, cost-basis summaries, alert settings, and status or error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json, skill.yaml, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

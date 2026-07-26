## Description: <br>
BottyFans lets agents operate creator monetization workflows, including profile setup, content publishing, media uploads, subscriptions, tips, direct messages, earnings tracking, and USDC payments on Base. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cartoonitunes](https://clawhub.ai/user/cartoonitunes) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to let an agent manage a BottyFans creator account, publish monetized content, communicate with fans, and coordinate USDC-based subscription, tip, and unlock workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can register accounts, publish public or paid content, send direct messages, configure webhooks, and initiate USDC payment workflows. <br>
Mitigation: Require explicit user approval before account creation, profile changes, posting, messaging, webhook setup, subscriptions, tips, unlock purchases, payment-intent submission, or on-chain transactions. <br>
Risk: The security summary notes real creator monetization and public-content workflows without clear user-confirmation boundaries. <br>
Mitigation: Run the skill with scoped credentials, review planned actions before execution, and keep payment and publishing operations behind human confirmation. <br>


## Reference(s): <br>
- [BottyFans ClawHub listing](https://clawhub.ai/cartoonitunes/skills/bottyfans) <br>
- [BottyFans API](https://api.bottyfans.com/api/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with JSON, TypeScript, and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes MCP configuration, REST API examples, and operational workflow guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

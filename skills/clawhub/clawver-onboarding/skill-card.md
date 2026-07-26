## Description: <br>
Set up a new Clawver store by registering an agent, configuring Stripe payments, customizing the storefront, creating products, and preparing operational integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and store operators use this skill to complete initial Clawver setup, including agent registration, Stripe onboarding, first product publication, seller linking, webhooks, and support feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can create or modify a real Clawver store, products, payments setup, webhooks, and feedback records. <br>
Mitigation: Review each command and run it only for the intended store and environment. <br>
Risk: CLAW_API_KEY, webhook secrets, and seller linking codes can grant access or enable account linking if exposed. <br>
Mitigation: Keep secrets private, avoid public logs, share linking codes only through a verified private channel, and regenerate short-lived codes when needed. <br>
Risk: Stripe onboarding requires identity and bank-account information from a human operator. <br>
Mitigation: Have the responsible human complete Stripe verification directly in the browser and confirm charges and payouts are enabled before publishing. <br>
Risk: Feedback submissions may include sensitive operational metadata. <br>
Mitigation: Redact metadata unless Clawver support needs it to reproduce or triage the issue. <br>


## Reference(s): <br>
- [Clawver Homepage](https://clawver.store) <br>
- [Clawver Documentation](https://docs.clawver.store) <br>
- [Clawver Agent API Reference](https://docs.clawver.store/agent-api) <br>
- [Clawver Status](https://status.clawver.store) <br>
- [Onboarding API Examples](references/api-examples.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/nwang783/skills/clawver-onboarding) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/nwang783) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash, JSON, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY for authenticated Clawver API calls and includes a human-required Stripe onboarding step.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; source frontmatter reports 1.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

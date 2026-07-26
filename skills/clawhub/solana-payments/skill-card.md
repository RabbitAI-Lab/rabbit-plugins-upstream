## Description: <br>
Create Solana-based USDC subscription checkout URLs with encoded parameters using the Tributary Payments SDK subscription session manager. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xeroc](https://clawhub.ai/user/xeroc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to create encoded Lando or Tributary checkout URLs for Solana USDC subscription payments and to check the required payment, redirect, tracking, and subscription parameters before sharing or redirecting customers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Checkout URLs can encode payment details that lead to incorrect recipients, amounts, billing frequency, gateway settings, redirect destinations, or unintended auto-renew behavior. <br>
Mitigation: Review each generated checkout URL and confirm the recipient public key, amount, fixed gateway, success and cancel URLs, billing frequency, and auto-renew setting before use. <br>
Risk: Tracking IDs and memos may include customer or payment metadata that is persistent or visible. <br>
Mitigation: Avoid placing sensitive customer data in tracking IDs or memos; use minimal unique identifiers suitable for payment reconciliation. <br>
Risk: The integration depends on npm packages for payment-session creation. <br>
Mitigation: Confirm the npm package source and pin dependency versions before installing or using the SDK. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xeroc/skills/solana-payments) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with TypeScript and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs checkout-session construction guidance; users supply amounts, Solana public keys, redirect URLs, tracking IDs, memo text, billing frequency, and auto-renew settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

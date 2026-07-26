## Description: <br>
Use the single ItPay entry point for human-directed ItPay buyer workflows covering service discovery, purchase, Checkout, delivery, recovery, and refunds; seller workflows are not implemented. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itpay](https://clawhub.ai/user/itpay) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use ItPay to discover purchasable services, collect required buyer input, present human Checkout, and recover delivery or refund state. The current release covers buyer workflows; seller workflows are not implemented. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses a local ItPay device identity under ~/.itpay-v3 for signed requests. <br>
Mitigation: Install only when that persistent local identity is acceptable, keep the identity private, and stop if device state is not writable instead of rotating or deleting it. <br>
Risk: ItPay workflows can lead to external service costs and payment authorization. <br>
Mitigation: Before Checkout, verify the service, price, required contact fields, and payment page with the human, then wait for explicit agreement before continuing. <br>
Risk: Telegram checkout buttons may be harder to review for non-Chinese users. <br>
Mitigation: Confirm the meaning of button labels and the Checkout page before treating any human action as authorization. <br>
Risk: Seller workflows are described as future work but are not implemented in this release. <br>
Mitigation: Use only buyer workflows and do not invent seller commands, onboarding, listings, or successful seller states. <br>


## Reference(s): <br>
- [ItPay OpenClaw Skill Repository](https://github.com/itpay-ai/itpay-skill-openclaw) <br>
- [ItPay CLI Buyer Quickstart](artifact/vendor/itpay-cli/docs/agent/buyer/quickstart.json) <br>
- [Human Checkout Handoff And Payment Verification](artifact/vendor/itpay-cli/docs/agent/buyer/payment-flow.json) <br>
- [Device Identity And Session Recovery](artifact/vendor/itpay-cli/docs/agent/buyer/identity-and-sessions.json) <br>
- [Agent Type And Checkout Handoff Rendering](artifact/vendor/itpay-cli/docs/agent/buyer/render-hosts.json) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and human-facing summaries of CLI results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-stream agent guidance; checkout URLs, QR handoffs, and authorization prompts are shown only when returned by the CLI.] <br>

## Skill Version(s): <br>
2.0.17 (source: server release metadata and bundle.lock.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

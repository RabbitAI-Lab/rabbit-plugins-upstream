## Description: <br>
Run an autonomous e-commerce store on Clawver by registering agents, listing digital and print-on-demand products, processing orders, handling reviews, and managing revenue. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and store operators use this skill to let an agent operate a Clawver store: onboarding, product publishing, print-on-demand flows, order and refund handling, review responses, webhooks, analytics, and platform feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can be guided to take broad real-store actions, including publishing products, changing prices, issuing refunds, responding publicly to reviews, registering webhooks, linking seller accounts, and starting payment or Stripe flows. <br>
Mitigation: Require explicit human approval before any live store, payment, refund, public response, webhook, seller-linking, or broad skill-update action. <br>
Risk: The skill requires CLAW_API_KEY for authenticated marketplace operations. <br>
Mitigation: Keep CLAW_API_KEY private, use the narrowest available scope, and avoid exposing it in logs, shared prompts, or public artifacts. <br>
Risk: Platform feedback reports may include operational metadata from live commerce workflows. <br>
Mitigation: Review metadata before sending feedback and remove secrets, customer personal data, or unnecessary business-sensitive details. <br>


## Reference(s): <br>
- [Clawver Marketplace skill page](https://clawhub.ai/nwang783/skills/clawver-marketplace) <br>
- [Clawver homepage](https://clawver.store) <br>
- [Clawver Agent API documentation](https://docs.clawver.store/agent-api) <br>
- [Marketplace API Examples](references/api-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with REST API examples, curl commands, and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY and can guide actions that affect live store operations, payments, products, refunds, reviews, webhooks, and seller links.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence; artifact frontmatter says 1.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

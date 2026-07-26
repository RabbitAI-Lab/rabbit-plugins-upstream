## Description: <br>
Sell print-on-demand merchandise on Clawver. Browse Printful catalog, create product variants, track fulfillment and shipping. Use when selling physical products like posters, t-shirts, mugs, or apparel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nwang783](https://clawhub.ai/user/nwang783) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, developers, and store operators use this skill to plan, create, configure, publish, and monitor Clawver print-on-demand products backed by Printful catalog and fulfillment workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Clawver API key to manage store products, designs, fulfillment, and related workflows. <br>
Mitigation: Use a scoped or revocable API key when available and install the skill only for agents that should manage a Clawver store. <br>
Risk: Plan approval can start credit-spending design and mockup generation work. <br>
Mitigation: Review the proposed plan before approval and use idempotency keys for generation requests to reduce duplicate paid work during retries. <br>
Risk: Publishing or webhook configuration can affect live storefront behavior. <br>
Mitigation: Confirm prices, variants, mockups, publish status, and webhook URLs before allowing live changes. <br>


## Reference(s): <br>
- [Clawver Store](https://clawver.store) <br>
- [Clawver Print On Demand on ClawHub](https://clawhub.ai/nwang783/skills/clawver-print-on-demand) <br>
- [Print-on-Demand API Examples](references/api-examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with curl command examples and API request JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAW_API_KEY for authenticated Clawver API operations.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release evidence; artifact frontmatter reports 1.3.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

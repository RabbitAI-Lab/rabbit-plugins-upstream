## Description: <br>
Connects to a WooCommerce store via the WPClaw Connector plugin to fetch orders and products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[magnum-opus-v1](https://clawhub.ai/user/magnum-opus-v1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Store operators and developers use this skill to let an agent check WooCommerce order details, search products, and verify WPClaw Connector status for a configured WordPress store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses WooCommerce store credentials and can return customer, order, product, stock, and pricing data. <br>
Mitigation: Use least-privilege credentials where possible, store secrets outside prompts and logs, and avoid exposing customer data unless the task requires it. <br>
Risk: Dependency drift could affect connector behavior over time. <br>
Mitigation: Install from a reviewed, locked dependency set and keep the connector updated. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/magnum-opus-v1/skills/wpclaw-lite) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, guidance] <br>
**Output Format:** [Plain text tool responses and Markdown setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WPCLAW_STORE_URL and WPCLAW_STORE_SECRET environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

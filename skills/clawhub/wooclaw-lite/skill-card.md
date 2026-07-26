## Description: <br>
Connects to a WooCommerce store via the OpenClaw Connector Lite plugin to fetch orders and products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[magnum-opus-v1](https://clawhub.ai/user/magnum-opus-v1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and store operators use this skill to let an agent check WooCommerce order details, search products, and verify connector health for a WordPress store running the OpenClaw Connector Lite plugin. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose WooCommerce customer, order, product, stock, and pricing data to an agent session. <br>
Mitigation: Install only for agents and users authorized to view WooCommerce data, and avoid order lookups in shared or untrusted chats. <br>
Risk: The store secret authorizes signed connector requests and should be treated as sensitive. <br>
Mitigation: Store OPENCLAW_STORE_SECRET securely, protect it like an API key, and configure OPENCLAW_STORE_URL only for an HTTPS store you control. <br>
Risk: Dependency hardening may be needed before production deployment. <br>
Mitigation: Review, update, or pin dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/magnum-opus-v1/skills/wooclaw-lite) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, API calls, configuration, guidance] <br>
**Output Format:** [Plain text status, search, and order summaries returned by agent tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OPENCLAW_STORE_URL and OPENCLAW_STORE_SECRET to connect to a configured WooCommerce store.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

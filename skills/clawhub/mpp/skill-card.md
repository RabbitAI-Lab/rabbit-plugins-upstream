## Description: <br>
Build with MPP (Machine Payments Protocol), an open protocol for machine-to-machine payments over HTTP 402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenequm](https://clawhub.ai/user/tenequm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design, implement, test, and audit HTTP 402 MPP payment flows for paid APIs, payment-gated content, MCP tool payments, pay-per-token streaming, and multi-rail payment integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill teaches automatic payment flows that can spend real funds. <br>
Mitigation: Prefer testnet or sandbox rails, set per-origin policies and spending limits, and require explicit approval before mainnet payments or unattended agent use. <br>
Risk: Examples involve wallet seeds, private keys, API keys, and .env-style secrets. <br>
Mitigation: Protect secrets with an approved secret store, avoid committing local configuration, and rotate exposed credentials. <br>
Risk: Global fetch polyfills can make payment handling broader than intended. <br>
Mitigation: Use standalone payment-aware fetch clients or restrictive origin policies unless a global polyfill is explicitly required. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/mpp) <br>
- [OpenClaw Homepage](https://github.com/tenequm/skills/tree/main/skills/mpp) <br>
- [mppx CLI](references/cli.md) <br>
- [MPP Core Protocol Specification](references/protocol-spec.md) <br>
- [mppx TypeScript SDK Reference](references/typescript-sdk.md) <br>
- [pympp Python SDK](references/python-sdk.md) <br>
- [mpp Rust SDK](references/rust-sdk.md) <br>
- [Sessions](references/sessions.md) <br>
- [Discovery and the Payments Proxy](references/discovery-and-proxy.md) <br>
- [Production Gotchas](references/production-gotchas.md) <br>
- [Tempo Payment Method](references/tempo-method.md) <br>
- [Stripe Payment Method](references/stripe-method.md) <br>
- [Lightning Payment Method](references/lightning-method.md) <br>
- [Custom Payment Methods](references/custom-methods.md) <br>
- [Payment HTTP Authentication Scheme IETF Draft](https://datatracker.ietf.org/doc/draft-ryan-httpauth-payment/) <br>
- [MPP Documentation](https://mpp.dev) <br>
- [Tempo Documentation](https://docs.tempo.xyz) <br>
- [Stripe MPP Documentation](https://docs.stripe.com/payments/machine/mpp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Examples may reference payment credentials, wallet material, API keys, and environment variables.] <br>

## Skill Version(s): <br>
0.9.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

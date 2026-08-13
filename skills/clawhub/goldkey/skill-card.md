## Description:

Preflight proposed agent actions with GoldKey Action Gate for a deterministic ALLOW, REVIEW, or BLOCK receipt, or integrate the feature-gated GoldKey Guard beta as an operator-controlled enforcement path for actual MCP, HTTPS, AgentCash, or supported Base/EVM calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noah-ing](https://clawhub.ai/user/noah-ing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to screen proposed agent actions, evaluate GoldKey paid utility calls, and configure Guard beta workflows for controlled MCP, HTTPS, AgentCash, and Base/EVM execution. It is intended for workflows where the user can verify live service state, payment mandates, wallet use, and local enforcement boundaries before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent toward paid x402, utility-pass, or Guard decisions involving wallet activity.

Mitigation: Require an explicit current mandate before any payment, package download, wallet signing, or child-key revocation, and verify endpoint, amount, wallet, and request body before proceeding.

Risk: Wallet signatures, access tokens, child keys, or private keys could be exposed if passed through prompts, command arguments, logs, or shell history.

Mitigation: Use the agent secret store or private mode-0600 files for secrets, inject one-use signatures temporarily, and keep private keys out of prompts and command arguments.

Risk: Guard beta is advisory if the local enforcer is not the exclusive path to the connector credential or wallet signer.

Mitigation: Remove direct routes to guarded connectors or signers and forward only an unexpired locally verified ALLOW from the operator-controlled enforcer.

Risk: Live identity, prices, terms, Guard availability, or package integrity may differ from the artifact.

Mitigation: Fail closed unless live catalog, OpenAPI routes, payment requirements, terms, and package hashes match the documented values.

## Reference(s):

- [GoldKey Guard Beta](references/guard-beta.md)
- [GoldKey Utility Pass and Scoped Keys](references/pass-and-keys.md)
- [ClawHub Skill Page](https://clawhub.ai/noah-ing/skills/goldkey)
- [x402scan Server Listing](https://www.x402scan.com/server/8447beac-d24b-434a-bd01-5abfdab53f84)
- [Poncho Action Gate Listing](https://tryponcho.com/tool/url_aHR0cHM6Ly9nb2xka2V5LWVkZ2Utc3RvcmVmcm9udC5ub2FoLWluZy53b3JrZXJzLmRldi92MS9hY3Rpb24tZ2F0ZQ)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces decision-handling guidance, live-state checks, payment probes, Guard setup steps, and credential-handling instructions for the agent.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

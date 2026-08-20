## Description:

Preflight proposed agent actions with GoldKey Action Gate or route feature-gated Guard beta enforcement for MCP, HTTPS, AgentCash, and supported Base/EVM calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noah-ing](https://clawhub.ai/user/noah-ing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to screen proposed tool, wallet, and paid-service actions before execution, or to configure GoldKey Guard beta when a local enforcer can be the exclusive connector or signer path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid Action Gate, component-tool, pass, or Guard operations can create nonrefundable payments or wallet-backed actions.

Mitigation: Verify the live endpoint, amount, chain, token, and recipient before use; require an explicit current mandate, use a dedicated low-balance wallet where appropriate, and reconcile ambiguous receipts before retrying.

Risk: Access tokens, wallet signatures, private keys, and child-agent keys could be exposed through prompts, shell history, logs, or noncanonical endpoints.

Mitigation: Keep secrets in the agent secret store or private mode-0600 files, avoid command arguments for sensitive values, and never send credentials or paid requests to noncanonical origins.

Risk: GoldKey Guard is only enforcement when the local enforcer is the exclusive path to the connector credential or wallet signer.

Mitigation: Remove bypass routes, keep signing material local, verify receipt signatures and policy state locally, and treat Guard as advisory if exclusive-path isolation is not in place.

## Reference(s):

- [GoldKey GitHub Repository](https://github.com/noah-ing/goldkey)
- [GoldKey ClawHub Skill Page](https://clawhub.ai/noah-ing/skills/goldkey)
- [GoldKey Guard Beta Reference](references/guard-beta.md)
- [GoldKey Utility Pass and Scoped Keys](references/pass-and-keys.md)
- [Action Gate x402scan Listing](https://www.x402scan.com/server/8447beac-d24b-434a-bd01-5abfdab53f84)
- [Action Gate Poncho Listing](https://tryponcho.com/tool/url_aHR0cHM6Ly9nb2xka2V5LWVkZ2Utc3RvcmVmcm9udC5ub2FoLWluZy53b3JrZXJzLmRldi92MS9hY3Rpb24tZ2F0ZQ)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include service decision receipts, payment requirement details, and local configuration steps; paid or wallet-backed actions require explicit user control.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

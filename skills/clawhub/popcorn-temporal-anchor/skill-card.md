## Description:

Obtain and verify paid, signed temporal evidence before a time-sensitive cross-node action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[violetclaire](https://clawhub.ai/user/violetclaire)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill when a wallet-enabled agent needs portable, signed time evidence before making a participant-local decision within a time-sensitive execution window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A wallet-enabled agent may make a small disclosed USDC payment to an external service for time evidence.

Mitigation: Require participant-local policy approval before payment and use the skill only where that payment is allowed.

Risk: A copied or redirected endpoint could provide evidence that is not canonical POPCORN evidence.

Mitigation: Pay only the challenged resource URL, require the resource URL to equal https://767-2676.com/v1/time, and verify the receipt against the published POPCORN keys and expected node identity.

Risk: Temporal evidence could be treated as authorization or a command rather than supporting evidence.

Mitigation: Treat receipts as bearer evidence only and keep task payloads, authorization, outcomes, and execution-window decisions participant-local.

Risk: Payment, signature validation, timing validation, or the local execution-window decision may fail.

Mitigation: Fail closed unless all required payment, receipt, key, identity, timing, and freshness checks complete successfully.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/violetclaire/skills/popcorn-temporal-anchor)
- [Publisher profile](https://clawhub.ai/user/violetclaire)
- [POPCORN agents homepage](https://767-2676.com/agents)
- [Canonical execution contract](https://767-2676.com/SKILL.md)
- [Current service offer](https://767-2676.com/agent/offer)
- [Verification keys](https://767-2676.com/.well-known/popcorn-keys.json)
- [Reusable receipt verifiers](https://github.com/violetclaire/popcorn-temporal-anchor/tree/main/verify)

## Skill Output:

**Output Type(s):** [guidance, API Calls, JSON, shell commands, code]

**Output Format:** [Markdown guidance with URLs, HTTP workflow steps, JSON receipt verification requirements, and code verifier references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides an agent to obtain and verify a signed temporal receipt; it does not make the receipt a command or authorization.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

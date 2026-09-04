## Description:

Verify settled payload-bound time checkpoints for time-sensitive cross-node actions that require execution-window checks or exact-byte signed witness intervals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[violetclaire](https://clawhub.ai/user/violetclaire)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to verify signed witness intervals, payload digests, and execution-window overlap before taking a time-sensitive cross-node action. It defaults to a public STOP sample before any optional live checkpoint request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live checkpoint use may involve an external network call and a small USDC payment.

Mitigation: Run the public sample first; only request a live checkpoint when participant-local policy explicitly permits the payment and network call.

Risk: A valid signature or overlapping interval could be mistaken for authorization.

Mitigation: Treat the checkpoint only as fingerprint and interval evidence; keep authorization decisions in participant-local policy.

Risk: Tampered or mismatched payload bytes can invalidate the evidence.

Mitigation: Verify the exact payload digest and nonce binding before evaluating time or action policy.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/violetclaire/skills/popcorn-temporal-anchor)
- [Human demonstration](https://767-2676.com/demo)
- [STOP packet](https://raw.githubusercontent.com/violetclaire/popcorn-temporal-anchor/main/examples/witness/evaluation-packet.production.json)
- [PROCEED packet](https://raw.githubusercontent.com/violetclaire/popcorn-temporal-anchor/main/examples/witness/evaluation-packet.proceed-002.production.json)
- [Expected outcomes](https://raw.githubusercontent.com/violetclaire/popcorn-temporal-anchor/main/examples/witness/evaluation-outcomes.json)
- [TypeScript verifier](https://github.com/violetclaire/popcorn-temporal-anchor/tree/main/verify/typescript)
- [Python verifier](https://github.com/violetclaire/popcorn-temporal-anchor/tree/main/verify/python)
- [Agent offer](https://767-2676.com/agent/offer)
- [Canonical skill](https://767-2676.com/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and expected text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes public sample verification steps and policy-gated guidance for optional live checkpoints.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

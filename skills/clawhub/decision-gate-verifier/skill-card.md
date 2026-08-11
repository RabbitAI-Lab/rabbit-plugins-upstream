## Description:

Decision Gate Verifier provides paid third-party checks that compare an agent's proposed action with its committed claim and return an oracle-signed PASS, REFUSE, or IN_DOUBT receipt anchored on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vaahl-dev](https://clawhub.ai/user/vaahl-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they need independent, paid verification that an agent's action stayed within a previously committed claim, especially for donations, payouts, autonomous spending, or irreversible releases. It is intended for workflows that need a reproducible third-party receipt rather than only a self-authored audit log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that payment documentation conflicts with actual on-chain wallet behavior.

Mitigation: Review the payment flow before installing, confirm each paid check explicitly, and treat signatures or approvals as financial authorizations.

Risk: The skill can cause autonomous agents to authorize paid checks using assets on Base.

Mitigation: Use a dedicated low-balance Base wallet and verify the registry and API endpoints before use.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/vaahl-dev/skills/decision-gate-verifier)
- [Decision Gate product page](https://soulscore.xyz/decision-gate)
- [Soulscore methodology](https://soulscore.xyz/methodology)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration, Shell commands]

**Output Format:** [Markdown guidance with Python examples and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The verifier flow can return structured receipt data with PASS, REFUSE, or IN_DOUBT verdicts.]

## Skill Version(s):

0.3.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

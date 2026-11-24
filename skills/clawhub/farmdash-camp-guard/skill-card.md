## Description:

Pre-sign DeFi security checks for AI agents: audit token allowances, review unsigned transaction envelopes and run route or position risk-sentinel checks. Returns pass/review/halt policy verdicts; never signs, broadcasts or claims on-chain RPC simulation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi agents and their operators use Camp Guard before a proposed transaction to inspect token approvals, unsigned transaction envelopes, and route or position risk, then decide whether to continue, review, or halt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial ClawScan review reports that risk checks may send wallet and unsigned transaction details to FarmDash without a privacy warning.

Mitigation: Review this data-sharing behavior before use, and submit wallet or unsigned transaction details only if that disclosure is acceptable.

## Reference(s):

- [FarmDash Camp Guard manual](https://www.farmdash.one/openclaw-skills/farmdash-camp-guard/SKILL.md)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, JSON]

**Output Format:** [Structured pass, review, or halt verdicts with flags and explanatory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks apply to supplied data; transaction simulation is not run.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

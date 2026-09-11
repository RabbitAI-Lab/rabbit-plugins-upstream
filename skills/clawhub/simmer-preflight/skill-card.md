## Description:

Simmer Preflight runs a read-only pre-trade readiness check that returns wallet identity, venue status, balance, exposure, and an ok_to_trade verdict for autonomous trading agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Simmer Preflight before automated trades to check wallet identity, venue readiness, spendable balance, open exposure, and whether a planned trade should proceed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SIMMER_API_KEY and uses it to access Simmer SDK/API account data.

Mitigation: Install and run it only when the Simmer publisher is trusted, and provide the API key only in environments intended for this skill.

Risk: Preflight output can reveal wallet, balance, and position information.

Mitigation: Treat logs and JSON output as sensitive trading data and redact them before sharing.

Risk: The skill is used in real-money trading workflows even though it is read-only.

Mitigation: Use the ok_to_trade verdict as a pre-trade safety signal, review blockers and warnings, and keep independent controls around actual order submission.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/simmer/skills/simmer-preflight)
- [Simmer Documentation](https://docs.simmer.markets)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable terminal summary or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SIMMER_API_KEY; output may include wallet, balance, exposure, blocker, warning, and alert data.]

## Skill Version(s):

0.3.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

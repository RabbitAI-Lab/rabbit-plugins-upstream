## Description:

Pre-trade readiness check for autonomous agents. One call returns wallet identity, venue status, spendable balance, open exposure, and a structured ok_to_trade verdict. Live real-venue trades auto-run this check and refuse when ok_to_trade is False.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simmer](https://clawhub.ai/user/simmer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous trading agents use this skill before trade submission to check wallet identity, venue readiness, spendable balance, exposure, and blocker codes. It supports safer real-venue trading workflows by surfacing an ok_to_trade verdict before order placement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SIMMER_API_KEY is required and should be treated as a sensitive credential.

Mitigation: Use the least-privileged key available, store it in a secret manager or protected environment variable, and avoid committing or printing it.

Risk: Full JSON preflight output can include wallet, balance, exposure, and risk information.

Mitigation: Restrict log access, redact sensitive fields when sharing output, and avoid writing raw preflight JSON to broadly accessible logs.

Risk: Dependency drift in simmer-sdk could change preflight behavior.

Mitigation: Pin simmer-sdk to a reviewed version or use a locked requirements file with hashes for higher-assurance deployments.

Risk: The v0 gas balance field is not populated from on-chain RPC and insufficient gas detection depends on structured risk alerts.

Mitigation: Verify POL or SOL balances through the dashboard or another trusted source before live trading.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/simmer/skills/preflight)
- [Simmer documentation](https://docs.simmer.markets)
- [Publisher profile](https://clawhub.ai/user/simmer)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text readiness summary or structured JSON from a Python CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit code 0 indicates ok_to_trade, 1 indicates blocked, and 2 indicates configuration errors.]

## Skill Version(s):

0.3.6 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Yansheng Fund Flow helps agents run a local demonstration of fund-flow, northbound-flow, and stock-level capital-flow analysis using deterministic simulated data.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to demonstrate financial fund-flow analysis workflows with synthetic values. It is not suitable for trading, investment reporting, or automated financial decisions without verified real market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake deterministic simulated financial figures for live market fund-flow data because the documentation includes a contradictory real-data source table.

Mitigation: Treat all outputs as demo-only, preserve the simulated-data disclosure, and avoid using the numbers for trading, investment, reporting, or automated financial decisions.

Risk: Financial-looking analysis could be over-relied on without verified market data.

Mitigation: Require verified real data retrieval and human review before using any output for financial conclusions or operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yansheng-fund-flow)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Plain text or JSON produced by a local Python script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are deterministic simulated financial figures and should remain clearly labeled as demonstration data.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

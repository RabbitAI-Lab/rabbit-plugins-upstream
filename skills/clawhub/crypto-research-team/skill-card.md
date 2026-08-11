## Description:

Tracks on-chain activity, market data, and project fundamentals to produce dated crypto research briefs using a coordinated team of specialized agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto analysts, researchers, and agent operators use this skill to coordinate collection of on-chain data, market data, and project fundamentals, then synthesize the findings into dated research briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured roles can perform broader actions than a narrow crypto brief generator, including file writes, memory operations, event publishing, scheduling, and MCP invocation.

Mitigation: Install only in environments where those capabilities are acceptable, and constrain tool access, scheduling, and output destinations before use.

Risk: Crypto research outputs may be incomplete, stale, or misleading if market, on-chain, or project data sources are wrong or unavailable.

Mitigation: Require dated briefs, source checks, and human review before using outputs for investment, trading, or operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/crypto-research-team)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown research briefs and concise agent guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be dated and cross-checked before use.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

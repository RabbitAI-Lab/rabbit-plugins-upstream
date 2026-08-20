## Description:

Gate Simmer/Polymarket tennis market entries on live tennis match state from the Live Tennis API, returning an observe-only trade/no-trade decision and suggested sizing factor without placing orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bensynapse](https://clawhub.ai/user/bensynapse)

### License/Terms of Use:

MIT

## Use Case:

Developers and trading-system builders use this skill to gate tennis market strategy entries against live score state, server, break-point status, and stopped-match conditions before sizing. It is decision support only and leaves execution to the calling framework.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Live Tennis API key and may require a Simmer API key for live-data market listing.

Mitigation: Install only when those credentials are acceptable for the environment, scope keys appropriately, and avoid exposing them in logs or shared configuration.

Risk: Live sports data can be missing, stale, delayed, or misresolved, which can make a gate decision unreliable.

Mitigation: Treat the output as decision support, verify the external data source, and set staleness thresholds to match the polling cadence and risk tolerance.

Risk: A trade/no-trade and sizing suggestion can be mistaken for financial advice or automated execution.

Mitigation: Keep execution in the calling framework, review decisions before using them with capital, and pair the gate with an independent probability and risk model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bensynapse/skills/simmer-tennis-live-gate)
- [Publisher profile](https://clawhub.ai/user/bensynapse)
- [Live Tennis API documentation](https://docs.livetennisapi.com)
- [Simmer markets](https://simmer.markets)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces observe-only gate decisions and suggested sizing factors; it does not submit, sign, or cancel orders.]

## Skill Version(s):

0.1.0 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

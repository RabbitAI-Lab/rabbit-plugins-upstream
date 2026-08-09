## Description:

Evaluates A-share stock and portfolio momentum from price-volume patterns and returns technical HOLD, WATCH, REDUCE, SELL, add-position, and rebound signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers analyzing A-share holdings use this skill to generate technical momentum diagnostics, position-risk signals, portfolio scans, and follow-up review guidance. Outputs are informational trading signals and do not replace the user's own financial review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HOLD, REDUCE, SELL, add-position, and rebound outputs could be mistaken for financial advice.

Mitigation: Treat outputs as informational technical signals and require user review before making any trading or portfolio decision.

Risk: Results depend on the local volume-price-screener skill and external market-data availability.

Mitigation: Review the dependency setup and data availability before relying on scans or diagnostics.

Risk: Broad triggers and sector-resonance downgrade logic may produce conservative or context-sensitive signals.

Mitigation: Review downgrade explanations and compare signals with broader market, sector, and position context.

## Reference(s):

- [Pattern Rules](artifact/references/pattern_rules.md)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Terminal text and Markdown-style guidance with score summaries, decision labels, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HOLD, WATCH, REDUCE, SELL, add-position, rebound, score, and risk-warning labels.]

## Skill Version(s):

0.1.2 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

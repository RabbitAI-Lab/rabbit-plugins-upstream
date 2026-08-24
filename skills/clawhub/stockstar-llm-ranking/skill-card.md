## Description:

Queries StockStar Technology Channel's public LLM call rankings and helps agents summarize daily or weekly model rankings, token volume, vendor, trend, and search matches.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stockstar1996](https://clawhub.ai/user/stockstar1996)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Chinese-language questions about StockStar/OpenRouter LLM call rankings, including top daily or weekly models, vendor placement, token volume, changes, and keyword search matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can contact tech.stockstar.com when activated.

Mitigation: Deployers should allow that network destination only when live StockStar ranking lookups are intended.

Risk: Broad activation phrases may trigger unnecessary lookups during ordinary GPT, Claude, or model-ranking discussions.

Mitigation: Narrow activation rules or confirm user intent before running the ranking command.

Risk: Ranking data can be unavailable or stale if the upstream page changes, fails, or has not updated.

Mitigation: Use the returned updated_at and status fields in user-facing answers, and avoid inventing ranking values when the command returns no data.

## Reference(s):

- [StockStar Technology Channel](https://tech.stockstar.com/)
- [ClawHub skill page](https://clawhub.ai/stockstar1996/skills/stockstar-llm-ranking)
- [ClawHub publisher profile](https://clawhub.ai/user/stockstar1996)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Chinese-language Markdown summaries backed by JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contact https://tech.stockstar.com/ when activated; ranking freshness depends on the upstream page.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

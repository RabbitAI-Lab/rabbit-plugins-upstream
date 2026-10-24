## Description:

Helps agents retrieve and summarize crypto news, coin sentiment, social trends, and macroeconomic events using OKX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

Crypto market researchers and agents use this skill to prepare news briefings, compare coin sentiment, and review upcoming economic events. It supports read-only news and sentiment research rather than trading or account management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News lookups require a live OKX credential profile rather than demo mode.

Mitigation: Install the CLI only if a live profile is acceptable; keep credentials private and use them only for authorized read-only queries.

Risk: A cross-skill workflow suggests reading account balances and positions to provide trading advice, despite account data being outside this skill's scope.

Mitigation: Require explicit user consent and the appropriate portfolio skill before accessing balances or positions; do not treat account access as part of a routine news lookup.

Risk: Sparse news results may be supplemented with web search, which can mix sources of differing reliability.

Mitigation: Clearly label OKX data and external web results and verify material claims before drawing conclusions.

## Reference(s):

- [Cross-Skill Workflows and Tool Reference](references/workflows.md)
- [OKX](https://www.okx.com)
- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-sentiment-tracker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown briefings and natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [News, sentiment, and economic-calendar results may be supplemented by clearly attributed web sources.]

## Skill Version(s):

1.4.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

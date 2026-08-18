## Description:

Queries StockStar Technology's public LLM ranking page for daily and weekly model call rankings, including token volume, vendor, percentage change, trend direction, and new-listing status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stockstar1996](https://clawhub.ai/user/stockstar1996)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch and summarize StockStar's LLM call-volume rankings, inspect daily or weekly leaders, and search for specific models or vendors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes an outbound request to StockStar when ranking data is requested.

Mitigation: Use it only in environments where outbound access to https://tech.stockstar.com/ is permitted and expected.

Risk: Ranking extraction depends on the public page structure and may fail or return no data if that page changes.

Mitigation: Report unavailable data or request failures to the user and do not invent ranking entries.

## Reference(s):

- [StockStar Technology Channel](https://tech.stockstar.com/)
- [ClawHub skill page](https://clawhub.ai/stockstar1996/skills/stockstar-llm-ranking)
- [ClawHub publisher profile](https://clawhub.ai/user/stockstar1996)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [JSON from CLI commands, then concise Chinese text or Markdown summaries for users]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live public ranking data from StockStar and reports failures or empty results instead of fabricating rankings.]

## Skill Version(s):

1.0.1 (source: server release metadata and changelog; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

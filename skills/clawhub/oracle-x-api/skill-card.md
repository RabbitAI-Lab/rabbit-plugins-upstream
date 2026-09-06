## Description:

Read live market intelligence from a running Oracle-X terminal, including prices, candles, technical zones, news analysis, macro regime, on-chain metrics, prediction-market odds, ownership data, and historical market memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to query a self-hosted Oracle-X financial terminal and to write code against its documented API. It helps agents retrieve timestamped market data, technical levels, news analysis, macro context, authenticated user-scoped views, and long-running analysis jobs without inventing unavailable data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The configured Oracle-X instance may be unavailable, degraded, stale, or unable to resolve a requested symbol.

Mitigation: Check instance health and report returned errors or stale timestamps directly instead of filling gaps from memory.

Risk: ORACLE_X_TOKEN is a live Supabase account credential for authenticated chat, watchlist, and job endpoints.

Mitigation: Read the token from the environment only, avoid writing it to files, URLs, or logs, and use public endpoints when authentication is not required.

Risk: Chat and analysis job endpoints may spend the operator's LLM or provider budget.

Mitigation: Use cached direct endpoints for simple lookups, check existing cached analyses before starting jobs, and reserve chat jobs for open-ended questions.

Risk: Market intelligence can be incomplete or unsuitable for trading decisions if treated as advice.

Mitigation: Present Oracle-X responses as retrieved terminal data with timestamps, source gaps, and refusal states rather than as independent financial advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yigtwxx/skills/oracle-x-api)
- [Oracle-X Homepage](https://github.com/Yigtwxx/OracleX)
- [Authentication](references/auth.md)
- [Endpoints](references/endpoints.md)
- [Recipes](references/recipes.md)
- [Examples](examples/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON summaries, Python examples, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve API timestamps, distinguish missing data from transport failures, and avoid exposing ORACLE_X_TOKEN.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Oracle-X API helps an agent read live market intelligence from a running Oracle-X terminal, including prices, technical levels, news analysis, macro context, on-chain data, ownership, and market memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agents use this skill to choose Oracle-X API endpoints and return live market intelligence from a trusted running instance without inventing unavailable market data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send requests, prompts, or credentials to the Oracle-X instance configured by ORACLE_X_URL.

Mitigation: Use only trusted Oracle-X instances, verify that localhost:8000 is actually Oracle-X before relying on the default, and keep ORACLE_X_TOKEN in environment variables only.

Risk: Market data may be unavailable, stale, or unresolved for a requested symbol.

Mitigation: Report API errors, stale flags, and timestamps as returned, and do not substitute remembered prices or recompute terminal-provided values.

Risk: Authenticated chat and analysis jobs can expose prompts to the configured server and spend the operator's model or provider budget.

Mitigation: Check status and cached analysis first, use simple read endpoints for factual lookups, and request authentication only for scoped endpoints that need it.

## Reference(s):

- [Oracle-X endpoint reference](references/endpoints.md)
- [Oracle-X authentication guide](references/auth.md)
- [Oracle-X multi-step reads](references/recipes.md)
- [Oracle-X GitHub repository](https://github.com/Yigtwxx/OracleX)
- [Oracle-X API on ClawHub](https://clawhub.ai/yigtwxx/skills/oracle-x-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTTP endpoint selections, curl commands, and Python example references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reachable Oracle-X instance; ORACLE_X_TOKEN is optional and only used for authenticated endpoints.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

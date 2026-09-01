## Description:

Provides agent guidance for using the OKX CLI to retrieve crypto news, sentiment, source-filtered articles, and macro-economic calendar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for OKX-backed crypto market intelligence, including news briefings, coin sentiment snapshots, sentiment trends, source-filtered article lookup, and macro calendar context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires live OKX API credentials on the user's machine.

Mitigation: Use a dedicated least-privilege or read-only OKX API profile, and do not place API secrets in agent chat or shell history.

Risk: Position-specific analysis can expose sensitive financial or account context when combined with other OKX skills.

Mitigation: Require an explicit user request before account- or position-specific analysis and avoid displaying unnecessary sensitive details.

Risk: The release includes an npm-based CLI install step that the security summary flags as under-disclosed.

Mitigation: Review the package source, publisher, and install command before use in controlled or production environments.

Risk: Economic-calendar results can be misleading when the required time-window parameters are omitted or inverted.

Mitigation: Use both lower and upper time bounds for future calendar queries and clearly state the queried window in user-facing summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-sentiment-tracker)
- [OKX homepage](https://www.okx.com)
- [Cross-Skill Workflows & MCP Tool Reference](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-producing OKX CLI commands and user-facing caveats for credentials, demo-mode errors, rate limits, and sparse data.]

## Skill Version(s):

1.4.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Provides agent guidance for using the OKX CLI to retrieve crypto news, coin sentiment, sentiment trends, source-filtered news, full article details, and macro-economic calendar data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to produce crypto market briefings, coin sentiment analyses, news searches, source-filtered article summaries, and economic calendar reports from OKX CLI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authenticated OKX API credentials and documents credential setup patterns that may expose secrets through shell history.

Mitigation: Use a dedicated read-only OKX API key, avoid passing secrets as command-line arguments, and rotate any key that was configured with exposed command history.

Risk: The skill directs agents toward live OKX profiles because the news module does not support demo mode.

Mitigation: Confirm before using a live profile and restrict credentials to the minimum permissions needed for read-only news and sentiment access.

Risk: The globally installed npm CLI persists locally and handles authenticated OKX requests.

Mitigation: Review the package before installation, install only in trusted environments, and remove or update the CLI when it is no longer needed.

## Reference(s):

- [OKX](https://www.okx.com)
- [Cross-Skill Workflows and MCP Tool Reference](references/workflows.md)
- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-sentiment-tracker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tables, summarized news items, sentiment ratios, trend observations, and economic calendar fields.]

## Skill Version(s):

1.4.7 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

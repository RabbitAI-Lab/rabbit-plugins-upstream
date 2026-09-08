## Description:

Searches Xiaohongshu, Douyin, and WeChat Official Accounts for recent discussions about a topic and helps an agent produce cross-platform social media research reports with optional JSON and HTML outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, brand operators, and market researchers use this skill to research Chinese social media discussion, trends, and brand or product sentiment across Xiaohongshu, Douyin, and WeChat Official Accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics and API credentials can be sent to RedFox and search providers.

Mitigation: Use a dedicated REDFOX_API_KEY, avoid unrelated X_API_KEY values in the environment, and do not submit confidential brand, product, or strategy terms.

Risk: Generated HTML reports may contain dynamic data that is not fully escaped.

Mitigation: Review generated HTML before sharing, and open reports only with explicit intent from trusted local output paths.

Risk: The skill writes JSON and HTML reports to the local filesystem.

Mitigation: Use a controlled output directory and inspect generated files before redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/cn-last30days-redfox)
- [Publisher profile](https://clawhub.ai/user/yuanyi-github)
- [Output rules and templates](artifact/references/output-rules.md)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)
- [RedFox service](https://redfox.hk?source=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown research report with inline links, plus JSON summaries and optional HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a REDFOX_API_KEY when available, writes reports to a local output directory, and may include platform engagement metrics and source links.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter declares 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

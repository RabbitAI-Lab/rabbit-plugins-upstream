## Description:

全球AI新闻简报 searches 11 social and media platforms for a keyword and helps an agent aggregate results into AI-generated summaries, topic clusters, sentiment analysis, cross-platform comparisons, terminal tables, and an interactive HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Market, PR, content, media, and research teams use this skill to investigate public discussion around a keyword, compare coverage across domestic and global platforms, and produce a structured intelligence brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and request metadata are sent to RedFoxHub and results are received from the covered third-party platforms.

Mitigation: Use only approved, non-confidential search terms; do not submit secrets, personal data, or regulated business topics unless that data flow is approved for the environment.

Risk: The skill depends on REDFOX_API_KEY for authenticated API access.

Mitigation: Keep REDFOX_API_KEY scoped and revocable, and do not hard-code or expose it in code, prompts, logs, or generated output.

Risk: Generated result and report files can preserve collected public/social platform data and source links.

Mitigation: Review local report contents and storage location before sharing, archiving, or moving the files into managed environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/global-ai-news-brief)
- [API 接口参考](artifact/references/api-reference.md)
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with terminal tables, JSON aggregation files, and interactive HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY. The data collection script writes normalized JSON locally, and the skill produces an HTML report under the skill output directory.]

## Skill Version(s):

1.0.0 (source: release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

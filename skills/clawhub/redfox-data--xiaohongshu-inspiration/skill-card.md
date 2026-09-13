## Description:

Xiaohongshu Content Inspiration Expert helps creators, content operators, brands, and MCNs find Xiaohongshu topic ideas through RedFox-backed viral note search, bulk exports, daily breakout lists, low-follower viral mining, account leaderboards, and benchmark account recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

External Xiaohongshu creators, content operators, brands, and MCN agencies use this skill for topic research, trend monitoring, bulk content data export, account leaderboard review, and benchmark account discovery. The skill relies on RedFox Xiaohongshu data and requires a RedFox API key for authenticated workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and some scripts look for REDFOX_API_KEY in shell configuration files.

Mitigation: Set REDFOX_API_KEY only for the current session when practical, avoid storing keys in shell profiles, and rotate or revoke any exposed key.

Risk: Generated HTML reports may use network-loaded browser assets and may expose report content when opened in a browser.

Mitigation: Open generated HTML reports only when you trust the source data and, until CDN and HTML-injection issues are fixed, prefer a restricted or offline browser context.

Risk: Local report and cache files can contain Xiaohongshu query results, account data, and exported analysis.

Mitigation: Store generated CSV, HTML, and JSON cache files only in intended locations, delete sensitive exports after use, and review files before sharing.

Risk: Subscription-style workflows can create recurring tasks that continue after the initial query.

Mitigation: Enable subscriptions only after confirming how to list, modify, and remove the scheduled task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/xiaohongshu-inspiration)
- [RedFox Hub](https://redfox.hk/?source=clawhub)
- [RedFox API Key Page](https://redfox.hk/settings/api-keys?source=clawhub)
- [README.en.md](artifact/README.en.md)
- [Hot Article Output Format](artifact/references/m1_hot_article_format.md)
- [Daily Viral Core Workflow](artifact/references/m3_core_workflow.md)
- [Low-Follower Viral API Specification](artifact/references/m4_api_spec.md)
- [Leaderboard API Documentation](artifact/references/m5_api_docs.md)
- [Leaderboard Scoring Rules](artifact/references/m5_score_rules.md)
- [Benchmark Account Report Template](artifact/references/m6_account_template.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses, JSON data, shell commands, and generated CSV or HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local cache and report files; authenticated workflows require REDFOX_API_KEY.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

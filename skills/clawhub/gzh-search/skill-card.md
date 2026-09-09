## Description:

公众号搜索爬虫通过关键词搜索近 30 天内的微信公众号文章，在终端展示结果并导出 CSV 和交互式 HTML 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Industry researchers, content creators, and competitive analysts use this skill to search recent WeChat public account articles by keyword, review ranked article metrics, and export data for trend, content, and competitor analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The interactive HTML report starts an unsecured local proxy that can use the configured RedFox API key.

Mitigation: Use a revocable RedFox API key, prefer --csv-only when interactive search is unnecessary, and stop the local server promptly after use.

Risk: The security summary identifies unsafe HTML generation risks in the interactive report path.

Mitigation: Review generated HTML before sharing it, avoid sensitive search terms, and treat report contents as untrusted until the publisher hardens HTML escaping.

Risk: The security guidance calls out wildcard CORS and missing proxy authentication.

Mitigation: Run the proxy only on trusted local machines and prefer a future release that adds proxy authentication and narrows CORS.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/gzh-search)
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Terminal text with generated CSV files and interactive HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires REDFOX_API_KEY; use --csv-only when an interactive HTML report is not needed.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

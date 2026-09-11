## Description:

Monitors new-energy vehicle brand mentions across Chinese web and social platforms, analyzes sentiment and influence, detects urgent issues, and prepares Feishu reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wenxiaoyu](https://clawhub.ai/user/wenxiaoyu)

### License/Terms of Use:

MIT

## Use Case:

External brand, communications, and operations teams use this skill to monitor new-energy vehicle brand reputation, review sentiment trends, and receive alerts for negative, viral, or crisis-related mentions. Developers or operators configure SerpAPI, Feishu, platform coverage, and thresholds before running scheduled or on-demand monitoring.

### Deployment Geography for Use:

Global, with primary coverage of Chinese-language automotive and social platforms.

## Known Risks and Mitigations:

Risk: Monitored brand queries are sent to SerpAPI and generated reports are sent to Feishu.

Mitigation: Install only when that external data sharing is acceptable, review applicable platform terms, and require confirmation before external alert delivery.

Risk: The skill combines shell execution with scheduled recurring runs.

Mitigation: Run under a non-privileged account and avoid system-wide timers unless they are necessary for the deployment.

Risk: API keys and webhook URLs are required for normal operation and examples include webhook-shaped values.

Mitigation: Replace example webhooks, keep SerpAPI keys and Feishu webhooks in a proper secret store, and avoid committing local configuration.

Risk: Persistent memory writes can retain monitoring reports and trend data.

Mitigation: Require confirmation before memory writes and limit stored data to what is needed for trend analysis.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wenxiaoyu/skills/brand-monitor)
- [README](artifact/README.md)
- [Skill Definition](artifact/SKILL.md)
- [Release Notes v1.2.0](artifact/RELEASE_NOTES_v1.2.0.md)
- [SerpAPI Usage Guide](artifact/crawler/SerpAPI使用指南.md)
- [Feishu Webhook Guide](artifact/获取飞书Webhook指南.md)
- [SerpAPI Documentation](https://serpapi.com/docs)
- [Feishu Bot Documentation](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and Feishu interactive card JSON, with crawler JSON results and shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May send reports or alerts to Feishu and save monitoring or trend data to memory when configured.]

## Skill Version(s):

1.2.0 (source: server release metadata, SKILL.md frontmatter, CHANGELOG dated 2026-02-27)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

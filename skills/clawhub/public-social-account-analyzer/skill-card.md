## Description:

Analyzes public Chinese social accounts on Bilibili, Douyin, Weibo, Xiaohongshu, and WeChat Official Accounts from a profile URL, nickname, handle, or exported CSV/JSON to summarize content strategy, posting rhythm, engagement, performance patterns, and comment themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckycat133](https://clawhub.ai/user/luckycat133)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, and content teams use this skill to audit public Chinese social accounts, bind a profile from a URL or nickname, and produce evidence-scoped findings about content strategy, cadence, engagement efficiency, high and low performers, and audience comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live login cookies or OAuth tokens and can save or reuse cookies when persistence is enabled.

Mitigation: Prefer unauthenticated public data or user-exported files; use authorized sessions only with informed consent, avoid persistent cookie storage unless needed, and clear cached cookies afterward.

Risk: The skill includes scraping and signing machinery that may interact with platform access restrictions or rate limits.

Mitigation: Respect access stops, keep partial evidence scoped, avoid bypassing login walls or verification, and bind any signing service to localhost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckycat133/skills/public-social-account-analyzer)
- [Workflow](references/workflow.md)
- [Metrics and Sampling](references/metrics-and-sampling.md)
- [Model Insights](references/model-insights.md)
- [Comment Insights](references/comment-insights.md)
- [Cookie Guide](references/cookie-guide.md)
- [Exceptions](references/exceptions.md)
- [Platform Comparison](references/PLATFORM_COMPARISON.md)
- [Bilibili Platform Notes](references/platforms/bilibili.md)
- [Douyin Platform Notes](references/platforms/douyin.md)
- [Weibo Platform Notes](references/platforms/weibo.md)
- [Xiaohongshu Platform Notes](references/platforms/xiaohongshu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports with evidence summaries, plus optional structured files and shell commands when running bundled collection or analysis scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scoped uncertainty notes, partial-coverage disclosures, and generated report artifacts.]

## Skill Version(s):

0.9.2 (source: server release metadata and VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

新闻流事件驱动选股系统 - 接收财经新闻输入，通过百度千帆API进行事件NLP分析，关联受益A股标的，输出事件驱动选股信号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, finance analysts, and quant developers use this skill to turn financial news or policy text into event classifications, affected sectors, beneficiary A-share candidates, risk factors, and a human-readable report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly auto-process chat or news content that may include confidential or regulated financial information.

Mitigation: Use the skill only by explicit invocation or in a dedicated approved channel, and do not submit confidential or regulated financial information.

Risk: The documented public deployment uses plaintext HTTP and root SSH administration.

Mitigation: Do not use the documented production deployment as written; add HTTPS, authentication, least-privilege deployment accounts, and clear consent notices first.

Risk: Generated stock-picking signals can be incorrect, incomplete, stale, or misleading.

Mitigation: Treat outputs as decision support only, review source data and confidence labels, and keep the investment disclaimer visible in downstream reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenxyzcyxpp/skills/wq-news-event-driven-stock-pick)
- [Event Taxonomy](references/event_taxonomy.md)
- [Web Dashboard Setup](references/web-dashboard-setup.md)
- [Output Template](templates/output_template.md)
- [Baidu Qianfan Chat Completions Endpoint](https://qianfan.baidubce.com/v2/chat/completions)
- [Event-Driven Dashboard](http://racingai.top/event-driven)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Structured JSON analysis that can be formatted into a Markdown stock-news report.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes event type, event summary, market impact, affected sectors, beneficiary stocks, risk factors, signal summary, confidence, and model metadata when available.]

## Skill Version(s):

1.0.0 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

当用户给出小红书关键词、赛道、人群、产品方向、笔记链接或 note_id 时，该 skill 帮助拆解爆款文案的标题钩子、开头方式、卖点表达、情绪词、内容结构、互动引导和可复用文案框架。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content strategists use this skill to analyze public Xiaohongshu notes or keyword search samples and turn visible patterns into reusable copywriting frameworks. It is intended for read-only content research and creative planning, not account operation or engagement automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Returned Xiaohongshu URLs may contain xsec_token query parameters that could be exposed in chats, logs, saved files, or forwarded outputs.

Mitigation: Review outputs before sharing or storing them, and prefer a revised skill version that strips sensitive query parameters from visible or persisted URLs.

Risk: The skill depends on a local SOCIALDATAX_API_KEY and Node/npm execution, so failed setup can interrupt the workflow.

Mitigation: Confirm the API key, Node.js, npm, and network access are available before use, and keep the API key out of generated reports and logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-viral-copy-breakdown)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis report with optional shell command examples and JSON-derived tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve returned sample fields, note missing fields without fabrication, and avoid claiming full-platform coverage.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

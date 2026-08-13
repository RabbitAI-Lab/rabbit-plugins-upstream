## Description:

当用户给出小红书关键词、赛道、人群、产品方向、笔记链接或 note_id，想拆解爆款文案的标题钩子、开头方式、卖点表达、情绪词、内容结构、互动引导和可复用文案框架时使用。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and content analysts use this skill to analyze Xiaohongshu keywords, niches, product directions, note links, or note IDs and produce reusable viral-copy breakdowns. It helps identify title hooks, openings, selling points, emotional wording, content structure, engagement prompts, and next-step analysis ideas from returned public samples or note details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Final reports may expose token-bearing XHS URLs, including xsec_token query parameters, when links are displayed, stored, or forwarded.

Mitigation: Review outputs before sharing and prefer a release that redacts xsec_token and similar query parameters in final answers while using full URLs only transiently when an API call requires them.

Risk: Analysis is limited to user-provided inputs and the samples or note details returned by the configured SocialDataX calls.

Mitigation: Treat conclusions as sample-specific, label missing fields, and avoid presenting the results as complete-platform findings or guaranteed traffic guidance.

Risk: The skill requires a user-provided SOCIALDATAX_API_KEY and local node/npm execution to call the SocialDataX package.

Mitigation: Keep the API key in the environment, do not include it in prompts or reports, and confirm node/npm availability before running the CLI commands.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-viral-copy-breakdown)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with optional shell command examples and JSON-derived analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should preserve available fields, label missing fields instead of inventing them, and avoid claims of complete platform coverage or guaranteed traffic outcomes.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

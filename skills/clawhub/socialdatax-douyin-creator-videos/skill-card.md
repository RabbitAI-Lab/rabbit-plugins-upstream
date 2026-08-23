## Description:

用于抖音达人数据、抖音达人作品、作品列表、图文列表、短剧/合集列表、近期发布、内容调研和创作者内容分析。覆盖 Douyin creator works and series，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, and developers use this skill to retrieve and summarize Douyin creator works, image/text posts, recent publishing activity, and short-drama series from SocialDataX. It supports creator benchmarking, account tracking, and content research through CLI or MCP tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an npx-based SocialDataX package, so dependency trust matters before execution.

Mitigation: Review the npm package as part of normal third-party package approval before running the CLI.

Risk: SOCIALDATAX_API_KEY is required for data calls and could be exposed if pasted into prompts, files, or logs.

Mitigation: Provide the key through the environment and avoid embedding it in commands, generated files, or shared transcripts.

Risk: Unbounded --all runs can consume API credits because the skill has no default item or page cap.

Mitigation: Use --max-items, --pages, or a recent --since-days window unless a full crawl is intentional.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON results from SocialDataX CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm; multi-page creator results include page_count, item_count, and next_page_token when returned.]

## Skill Version(s):

0.1.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

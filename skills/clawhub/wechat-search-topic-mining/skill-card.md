## Description:

围绕一个关键词做微信生态选题挖掘，综合搜索结果、微信指数相关结果、热门文章和联想推荐词，形成选题清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content strategy operators use this skill to evaluate whether a WeChat topic direction is worth pursuing, inspect related article heat, and expand long-tail keyword angles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores a We-Media API key locally and sends queries to api.we-media.cn.

Mitigation: Install and use it only when local key storage and We-Media API query submission are acceptable for the intended workflow.

Risk: Local files may be uploaded when --file, videoUrl, or audioUrl points to a local path.

Mitigation: Pass those values only after confirming that the specific file should be uploaded to the We-Media service.

Risk: Paid multi-page requests can cost more than the displayed estimate indicates.

Mitigation: Review the requested page count before adding --yes, and verify the emitted consumption and balance markers after execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-search-topic-mining)
- [We-Media API site](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, or Excel files with terminal status markers and optional report-style Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Excel output requires openpyxl; paid calls emit consumption and balance markers.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence; bundled frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

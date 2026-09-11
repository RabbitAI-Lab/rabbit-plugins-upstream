## Description:

批量导出指定小红书博主主页「笔记」tab 的全部公开笔记为本地 Markdown（每篇含标题/原文链接/正文/图片与视频 URL/互动数赞藏评），支持 count/offset/parallel。

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content researchers use this skill to archive public Xiaohongshu creator notes as local Markdown for personal study, competitive analysis, backup, or downstream AI analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The exporter uses a logged-in Chrome session through a local relay and creates persistent local copies of Xiaohongshu public note content, links, media URLs, and engagement metadata.

Mitigation: Run it only for content you are authorized to archive, choose a controlled output directory, and review retained files before sharing or uploading them.

Risk: The package includes an unrelated obfuscated LLM helper that is not disclosed by the skill instructions.

Mitigation: Review carefully before installing and wait for the publisher to remove the helper or clearly document why it is present and how it is controlled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fatmind/skills/xhs-note-batch-export)
- [WebClaw3 setup site](https://webclaw3.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Local Markdown files, summary JSON files, and one-line JSON status on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates one Markdown file per exported note plus summary.json, res.json, and data.md in the selected output directory.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

查询抖音公开视频、账号、作品、评论和热榜数据，并以结构化 JSON 输出，支持短视频选题、竞品研究和舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

短视频运营、内容分析和市场研究人员可用它检索抖音公开视频与账号、查看作品和评论、追踪热榜，并将结构化数据用于选题、竞品和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign with medium confidence, but coverage was partial: 58.5% scanned and 22 files only partly inspected.

Mitigation: Review the skill and its files before installation; treat the scan as partial evidence, not a safety guarantee.

Risk: Supplied Douyin links or IDs and keyword-based account searches are sent to a third-party API.

Mitigation: Submit only public content references and search terms you are comfortable sharing with GUAIKEI, and use data you are authorized to analyze.

## Reference(s):

- [使用说明与命令参考](readme.md)
- [参数选项](references/options.md)
- [错误处理与重试说明](references/errors.md)
- [GUAIKEI 官网与支持](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON data with concise text analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Douyin data; requires GUAIKEI_API_TOKEN. Supplied search terms and links are sent to GUAIKEI's service.]

## Skill Version(s):

1.5.0 (source: release evidence, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

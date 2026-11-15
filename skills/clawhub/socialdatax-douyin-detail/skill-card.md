## Description:

用于抖音数据分析、抖音作品详情、图文详情、作品数据、互动指标、内容调研和内容分析。覆盖 Douyin work details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要分析抖音内容的用户，查询单个视频或图文作品的描述、作者、发布时间、互动指标及可用媒体信息。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner classifies this release as suspicious because it uses an unpinned, automatically confirmed CLI package, creating a supply chain risk. Analysis is partial because local references were unresolved; no malicious behavior was established.

Mitigation: Review and trust the publisher and package before installing; prefer a reviewed, pinned version over @latest, and limit the files and credentials available to the CLI.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub release page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-detail)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured Douyin work detail data summarized in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields vary by post; may include content, author, publish time, interaction counts, images, video, music, and media summary.]

## Skill Version(s):

0.1.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

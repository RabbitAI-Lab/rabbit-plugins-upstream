## Description:

当用户需要做好看视频选题、短视频内容方向规划或竞品角度复盘时使用。基于用户提供的主题或视频链接，整理相关作品、标题角度与评论反馈，输出带样本依据的选题清单。来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向外部内容创作者及视频运营人员，按主题或已有作品分析好看视频的标题角度与评论反馈，并整理有样本依据的候选选题、目标受众和内容方向。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 搜索关键词及视频链接或 ID 会交由 SocialDataX 处理，并可能消耗服务额度。

Mitigation: 避免提交机密内容；确认输入适合交由该服务处理，并按需要限制查询范围。

Risk: 运行需要 SocialDataX API Key。

Mitigation: 通过 SOCIALDATAX_API_KEY 环境变量提供密钥，不要将其写入技能文件、命令记录或共享输出。

Risk: 使用未固定版本的 CLI 依赖可能带来版本变化。

Mitigation: 优先使用已审查并固定版本的 CLI，而不是 @latest。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/haokan-topic-analysis)
- [SocialDataX service and API key information](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [选题清单可包含目标受众、内容角度、参考标题、优先级、理由及可见作品依据；样本数量、观察时间和缺失信息按实际结果说明。]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

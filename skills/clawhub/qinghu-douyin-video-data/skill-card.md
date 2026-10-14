## Description:

通过青虎数据查询抖音视频链接的作者、播放量、互动数据、标题、音乐及发布时间。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营人员和分析人员可通过抖音视频链接查询播放量、互动指标及基本信息，并生成简要结果摘要。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 自动安装或升级本地运行时和 npm 包可能改变环境，且安装命令未固定依赖版本。

Mitigation: 优先使用预装且固定版本的 qhkit；安装或升级前先审核命令，避免让技能自动修改 shell 启动文件。

Risk: 查询需要青虎账户密钥，付费调用可能产生随返回量增加的积分费用。

Mitigation: 保护密钥；调用前核对预计费用并取得用户同意，批量查询时限制调用次数并报告实际消耗。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-douyin-video-data)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎AI API 密钥](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [简要文字或 Markdown 摘要；结果较多时提供表格文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [报告视频指标和实际消耗的青虎积分；查询失败时说明错误。]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

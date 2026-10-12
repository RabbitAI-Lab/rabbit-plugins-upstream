## Description:

按作品 ID、搜索结果 ID 或分享短链查询微信视频号作品详情。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

视频号内容运营人员和其他用户通过作品 ID 或分享短链获取作品详情，用于查看和分析视频数据。查询使用付费的青虎数据服务。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid lookups can incur credits, including some failed calls.

Mitigation: Check the current estimate and obtain user approval before paid calls; avoid repeated trial-and-error calls.

Risk: Persistent token configuration can expose API credentials.

Mitigation: Prefer a platform secret or environment variable over storing the token in local configuration.

Risk: Installing or upgrading qhkit or Node can alter the local environment.

Mitigation: Prefer a sandbox or preinstalled tooling and review install or upgrade commands before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-video-data)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [青虎数据 API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Chinese-language summary; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits spent on paid calls; large result sets may be delivered as files.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

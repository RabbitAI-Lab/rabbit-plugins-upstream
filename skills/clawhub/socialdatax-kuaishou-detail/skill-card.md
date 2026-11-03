## Description:

用于快手（Kuaishou / Kwai）作品详情查询、互动指标查看及内容调研分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容分析人员和研究者可用它查询 Kuaishou / Kwai 作品详情及互动指标，并整理内容调研信息。用户提供作品 ID 或链接后，技能可返回结构化详情，也可按请求保存媒体。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be exposed during configuration or use.

Mitigation: Keep the API key in trusted secret storage and out of chat and version control.

Risk: The external npm package implementation was not inspected.

Mitigation: Prefer a reviewed, pinned CLI version or an already configured MCP connection.

Risk: Optional media downloads write to a local destination.

Mitigation: Choose the output path explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-detail)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON data, Text, Shell commands, Configuration guidance]

**Output Format:** [Structured JSON details with concise text guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields depend on available work details; saving media is optional.]

## Skill Version(s):

0.1.21 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

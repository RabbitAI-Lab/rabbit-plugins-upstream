## Description:

查询微信视频号账号主页资料和统计信息，辅助账号画像与运营分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and operators use this skill to retrieve WeChat Channels profile details and statistics for account assessment and operational analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation steps may change the local Node/npm environment or persist shell configuration.

Mitigation: Review installation steps and prefer a preinstalled, pinned qhkit version in a contained environment.

Risk: Configuring qhkit requires sharing a Qinghu API token with the CLI.

Mitigation: Use only a token intended for qhkit and keep it out of logs and shared files.

Risk: Profile lookups may consume paid Qinghu credits.

Mitigation: Check the current estimate and obtain user approval before paid calls.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-profile)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise Markdown profile summary; tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports credits consumed by paid calls and distinguishes full results from previews.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

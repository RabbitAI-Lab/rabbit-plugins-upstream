## Description:

用 Cue 穿透目标行业的景气周期、竞争格局与产业链地位，识别集中度、龙头壁垒与供需/政策拐点，研判当前所处周期位置与投资机会窗口，产出可支撑配置决策的行业研判底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, investment researchers, and strategy teams use this skill to request a structured industry research brief covering business cycle position, competitive landscape, supply-demand inflection points, policy catalysts, value-chain position, and investment window assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local Cue runner is unaudited and unpinned, and can access the user's Cue API key and filesystem.

Mitigation: Review and pin the runner revision before use, run it only under a user account and directory scope appropriate for the task, and use a narrowly scoped or revocable Cue API key where possible.

Risk: The skill depends on Cue service availability and external data sources for report quality and freshness.

Mitigation: Run the documented health checks before research, review source links in the generated report, and retry or use documented fallback sources when Cue or public sources are unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-industry-competition)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Example Cue report](https://cuecue.cn/share/RWtYmuF_)
- [Cue API key page](https://cuecue.cn/hub/api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research brief with source links and optional shell commands for execution or format conversion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write report files to a user-specified output path; quality and freshness depend on Cue service availability and external data sources.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

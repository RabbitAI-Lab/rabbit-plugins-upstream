## Description:

用用户显式提供的 accessToken 调用 WorkBuddy 官方签到接口，领取每日积分并汇报结果；脚本幂等、零依赖（仅 Python 标准库），只访问官方白名单域名，不读取也不写入本机客户端凭据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[oracis](https://clawhub.ai/user/oracis)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy 用户可在明确要求签到或查询积分时，用此技能领取每日积分并查看签到状态。若用户只提到签到或领积分而未说明平台，应先确认是否指 WorkBuddy。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the release suspicious over interpreter validation that could allow an untrusted executable to run under a scheduled-task account; the analysis is partial.

Mitigation: Review interpreter validation and the permissions granted to scheduled scripts before installation; several local references were not matched by the scan.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/oracis/skills/workbuddy-checkin)
- [Project homepage](https://github.com/oracis/workbuddy-checkin)
- [WorkBuddy service](https://www.workbuddy.cn)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Concise status text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports activity, streak, points, and whether today's check-in succeeded or was already complete.]

## Skill Version(s):

1.5.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

按直播间 ID 查询微信视频号直播间详情，并向用户汇总结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting users who need details for a specified WeChat 视频号 live room use this skill to retrieve and summarize the room data with the paid Qinghu service after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can install or update Node.js and qhkit locally and requires a Qinghu API token.

Mitigation: Confirm local installation and token use before setup; prefer a controlled or pinned installation when reproducibility matters and protect the token.

Risk: Live-room lookups are paid and repeated calls can incur Qinghu credits.

Mitigation: Estimate credits and get user approval before paid calls; limit calls to the requested live-room details and report actual credits used.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-live-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise written summary with key live-room details; optional tabular file for larger results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits used for paid calls; retrieved data depends on the requested live_id.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

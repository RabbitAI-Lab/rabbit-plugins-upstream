## Description:

查询中国国内法律法规及行政令，并整理立法背景、合规要点和可回查出处。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

企业法务、合规人员和个人可用自然语言查询中国法规、行政令和相关立法资料，并获取条款解读、合规要点及来源链接。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill installs and updates an external runner whose code can change.

Mitigation: Inspect and pin the runner to a specific revision, and require approval before updates.

Risk: API-key setup instructions could expose a credential if the key is shared in chat or stored without access controls.

Mitigation: Keep the key in protected local storage, restrict its file to the owner, and do not send it through chat.

Risk: Legal questions or shared report links may expose confidential details.

Mitigation: Remove confidential details before submitting questions and check report-link visibility before sharing.

## Reference(s):

- [Cue Playbook](https://cuecue.cn/playbook)
- [National Laws and Regulations Database](https://flk.npc.gov.cn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese structured research report with legal citations and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves legal names and article numbers; includes sources for follow-up verification.]

## Skill Version(s):

1.0.10 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

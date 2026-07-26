## Description: <br>
五平台协同运营工具包——管理跨平台（虾聊/AIWay/MEYO/贴吧/钉钉）的多账号协同发帖、交叉引用、数据采集与复盘。适合做多平台内容运营的 AI Agent。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bdz2007-antgroup](https://clawhub.ai/user/bdz2007-antgroup) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations teams and agent operators use this skill to coordinate multi-account posting, cross-platform engagement, metrics collection, and review workflows across ClawdChat, AIWay, MEYO, Tieba, and DingTalk. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent to coordinate posting, commenting, likes, messages, scheduling, and data collection across real accounts. <br>
Mitigation: Use only accounts the operator is authorized to control and require explicit approval before any posting, commenting, liking, messaging, or schedule changes. <br>
Risk: The cycle-state file can contain sensitive campaign, account, post, and scheduling metadata. <br>
Mitigation: Store cycle-state data in an access-controlled location and avoid exposing it in public logs, prompts, or shared artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bdz2007-antgroup/skills/multi-platform-synergy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with JSON state examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce content plans, operational checklists, metric summaries, and cycle-state JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

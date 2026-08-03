## Description: <br>
积分红包一键领取·全平台自动化省心神器。以「领取规划 + 场景识别 + 定时任务 + 学习反馈」四大模块为核心，开箱即用 WorkBuddy 每日积分，截图或视频学习任意 APP 签到场景，三重保障防漏领。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this Windows-only skill to automate daily WorkBuddy points, sign-in, and gift-claiming workflows, check for missed claims, and learn new claim scenes from screenshots or short videos. It is intended for lawful, user-authorized reward collection where the final reward status remains determined by the target platform. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect screenshots and interact with desktop applications, which may expose sensitive information or perform unintended clicks. <br>
Mitigation: Use it only on authorized screens, avoid sensitive personal or financial content during automation, and review claim results before relying on them. <br>
Risk: The skill can create recurring scheduled tasks for unattended automation. <br>
Mitigation: Enable scheduled tasks only after explicit confirmation, review Windows Task Scheduler entries regularly, and disable tasks that are no longer needed. <br>
Risk: The skill stores local learning history and scene data that may include details from prior claim workflows. <br>
Mitigation: Review learned data periodically, keep the data directory access-controlled, and remove stale or sensitive learned scenes. <br>
Risk: Dispatcher calls have weak scoping, which can broaden what underlying gift-domain tools may be invoked. <br>
Mitigation: Review configured tools and parameters before deployment and prefer narrow, user-approved automation flows. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/workbuddy-gift-claimer) <br>
- [Flow Immersion Related Skill](https://skillhub.cn/skills/user_11064e10/flow-immersion) <br>
- [WorkBuddy Tuner Related Skill](https://skillhub.cn/skills/user_11064e10/workbuddy-tuner) <br>
- [Privacymask Related Skill](https://skillhub.cn/skills/user_11064e10/privacymask) <br>
- [Tax Policy Knowledge Related Skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown-style status reports, claim summaries, learned scene configuration summaries, scheduled-task status, and next-step guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reflect local OCR results, local claim history, learned scene data, and Windows scheduled-task state.] <br>

## Skill Version(s): <br>
2.4.0 (source: frontmatter, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

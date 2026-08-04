## Description: <br>
积分红包一键领取·全平台自动化省心神器。以「领取规划 + 场景识别 + 定时任务 + 学习反馈 + 每日汇总」五大模块为核心，开箱即用 WorkBuddy 每日积分，截图或视频学习任意 APP 签到场景，三重保障防漏领，每日自动生成汇总报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to automate WorkBuddy and similar daily reward, sign-in, and points-claiming workflows, including claim planning, learned scene recognition, scheduled claiming, missed-claim checks, and daily summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Desktop UI automation can click in local applications and may affect accounts, rewards, or app state if used on the wrong window. <br>
Mitigation: Use explicit prompts, keep the intended app visible, review learned scenes before repeated use, and stop execution if the active window is unexpected. <br>
Risk: The skill keeps local claiming history, scene data, and learned coordinates. <br>
Mitigation: Use a user-controlled data directory, periodically review stored state, and remove records that reveal sensitive app or account context. <br>
Risk: First use may download OCR assets and scheduled claiming may install a Windows task. <br>
Mitigation: Allow the OCR download only on trusted networks and review or disable the scheduled task if automatic claiming is no longer desired. <br>
Risk: Bulk skill-matrix installation can add related skills beyond this claimer. <br>
Mitigation: Install related skills individually unless the user intentionally wants the broader skill matrix. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/workbuddy-gift-claimer) <br>
- [Flow Immersion related skill](https://skillhub.cn/skills/user_11064e10/flow-immersion) <br>
- [WorkBuddy Tuner related skill](https://skillhub.cn/skills/user_11064e10/workbuddy-tuner) <br>
- [Privacymask related skill](https://skillhub.cn/skills/user_11064e10/privacymask) <br>
- [Tax Policy Knowledge related skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, status text, JSON-like summaries, configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe claiming results, learned scene configuration, scheduled task status, failure reasons, and daily summary reports.] <br>

## Skill Version(s): <br>
2.5.0 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

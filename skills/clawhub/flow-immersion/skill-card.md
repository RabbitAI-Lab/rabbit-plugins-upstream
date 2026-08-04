## Description: <br>
番茄钟专注神器，ADHD陪伴 + 沉浸环境 + 桌面控制，离线可用。配套本地 H5 沉浸界面，支持番茄双段计时、微步骤拆分、多巴胺菜单、紧急协议、复盘引导、八大壁纸预设、任务规划与提醒、专注统计与报告。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who use ClawHub agents for work or study use this skill to run Pomodoro-style focus sessions, break tasks into smaller steps, plan work blocks, generate reminders, and review focus statistics. It also supports immersive desktop environment changes such as wallpaper presets, hidden desktop icons, and a local H5 focus interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Desktop integration may change wallpaper, desktop icon visibility, or window state. <br>
Mitigation: Require clear user confirmation before desktop changes and provide a restore path for prior desktop settings. <br>
Risk: Focus, planning, reminder, and statistics history may reveal sensitive work patterns or personal routines. <br>
Mitigation: Store only necessary local history, document sync behavior, and avoid sending broad local state unless the user has explicitly enabled it. <br>
Risk: The security evidence reports that backend state sharing and desktop-changing behavior are not scoped or disclosed clearly enough for automatic approval. <br>
Mitigation: Review the skill before installing and ask the publisher to narrow triggers, require confirmation for desktop changes and bulk skill installation, and minimize backend state sharing. <br>


## Reference(s): <br>
- [Flow Immersion ClawHub listing](https://clawhub.ai/zxj2devs/skills/flow-immersion) <br>
- [WorkBuddy Tuner related skill](https://skillhub.cn/skills/user_11064e10/workbuddy-tuner) <br>
- [WorkBuddy Gift Claimer related skill](https://skillhub.cn/skills/user_11064e10/workbuddy-gift-claimer) <br>
- [Privacymask related skill](https://skillhub.cn/skills/user_11064e10/privacymask) <br>
- [Comprehensive tax policy knowledge related skill](https://skillhub.cn/skills/user_11064e10/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and text responses with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May coordinate local focus-session state, planning data, reminders, statistics, and desktop-environment actions when the host environment supports them.] <br>

## Skill Version(s): <br>
5.3.0 (source: frontmatter, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

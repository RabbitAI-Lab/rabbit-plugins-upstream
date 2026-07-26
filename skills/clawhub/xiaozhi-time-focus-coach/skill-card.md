## Description: <br>
A Chinese-language study coach that helps students record learning time, run guided Pomodoro focus sessions, analyze distraction patterns, and build focus-history summaries with user consent. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students use this skill to understand where study time goes, plan realistic focus windows, and improve concentration through consent-based logs, Pomodoro check-ins, and follow-up summaries. It is also useful for study-planning agents that need user-approved focus-pattern summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Long-term focus logs can reveal study habits, distraction patterns, and productivity routines. <br>
Mitigation: Enable archives, reminders, or sharing summaries only with user confirmation, and make clear when conclusions rely on lower-confidence self-reported timing data. <br>
Risk: Users may overread completion metrics as proof of learning quality or as an attention assessment. <br>
Mitigation: Frame completion rates as behavior indicators, combine time data with learning-quality signals, and recommend professional evaluation when persistent attention problems substantially affect daily learning or social life. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-time-focus-coach) <br>
- [Focus archive template](artifact/references/focus-archives-template.md) <br>
- [Pomodoro state machine](artifact/references/pomodoro-statemachine.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown conversation responses with structured study-time logs, focus-session check-ins, and summary templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update user-approved focus archives, Pomodoro session records, and reminder handoffs when platform support exists.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

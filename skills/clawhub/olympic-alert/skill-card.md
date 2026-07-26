## Description: <br>
Olympic Alert checks a local Olympic event schedule and produces reminders up to 15 minutes before configured events, with commands to list, add, and remove events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garibong-labs](https://clawhub.ai/user/garibong-labs) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users and agents use this skill to manage and monitor Olympic event schedules, especially 2026 Milano Cortina Winter Olympics events configured for the Korea team. It can be invoked manually or from a heartbeat workflow to return timely reminder text and broadcast links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The add and remove commands modify the local schedule file, and removal is based on name-pattern matching. <br>
Mitigation: Review schedule changes before relying on reminders, and use specific event-name patterns when removing events. <br>
Risk: Reminder delivery depends on an agent heartbeat or other scheduler invoking the local checker at the right time. <br>
Mitigation: Configure a heartbeat or scheduler to run the check command regularly and verify that it reports expected upcoming events. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/garibong-labs/skills/olympic-alert) <br>
- [Naver Sports Milano Cortina 2026](https://m.sports.naver.com/milanocortina2026) <br>
- [Chzzk Olympic search](https://chzzk.naver.com/search?query=올림픽) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Plain text and Markdown reminders with inline links, plus command-line status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Python 3 and local JSON schedule and state files; no additional packages are required.] <br>

## Skill Version(s): <br>
0.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

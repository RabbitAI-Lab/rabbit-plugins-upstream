## Description: <br>
Monitors Korean IPO subscription and new-listing schedules from 38.co.kr and produces D-1, day-of, and weekly summary alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[garibong-labs](https://clawhub.ai/user/garibong-labs) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to monitor Korean IPO subscription and new-listing schedules, receive timely reminders, and produce weekly summaries from public 38.co.kr data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs periodic requests to 38.co.kr when scheduled through cron or heartbeat automation. <br>
Mitigation: Review the cron or HEARTBEAT schedule and run it only as often as intended. <br>
Risk: The skill stores prior alert history in ~/.config/ipo-alert/state.json. <br>
Mitigation: Inspect or delete the state file when resetting alert history or when local state retention is not desired. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/garibong-labs/skills/ipo-alert) <br>
- [38.co.kr IPO subscription schedule](https://www.38.co.kr/html/fund/index.htm?o=k) <br>
- [38.co.kr new listing schedule](https://www.38.co.kr/html/fund/index.htm?o=nw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown/plain text alerts and Korean schedule summaries with command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and curl; may write ~/.config/ipo-alert/state.json to suppress duplicate alerts.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

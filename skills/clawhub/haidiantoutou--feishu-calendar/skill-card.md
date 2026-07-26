## Description: <br>
Manage and sync Feishu calendars, list and search calendars, check schedules, mark tasks, and set up shared project calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent inspect Feishu calendars, create reminder or task events, synchronize upcoming schedule state, and configure shared project calendars. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete live Feishu calendar events, including routines that affect future calendar entries. <br>
Mitigation: Use a dedicated test calendar first, confirm each target calendar ID and event visibility setting, and avoid setup, cleanup, or sync routines until their behavior is acceptable. <br>
Risk: Calendar access falls back to primary calendars when a selected calendar is unavailable, which can affect unintended calendar data. <br>
Mitigation: Configure a least-privilege Feishu app and verify calendar permissions so the agent can access only the intended calendar scope. <br>
Risk: The skill requires Feishu app credentials in environment configuration. <br>
Mitigation: Store FEISHU_APP_ID and FEISHU_APP_SECRET separately from unrelated workspace secrets and rotate them if exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/feishu-calendar) <br>
- [Publisher profile](https://clawhub.ai/user/haidiantoutou) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and console text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, update, list, or delete Feishu calendar data when the referenced Node scripts are run with configured credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

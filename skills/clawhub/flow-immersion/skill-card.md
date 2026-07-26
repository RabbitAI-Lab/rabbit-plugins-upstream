## Description: <br>
Flow Immersion helps users configure focus sessions with Pomodoro timers, ADHD-oriented companion workflows, health reminders, an immersive local web interface, and focus history tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who want structured focus support use this skill to select or customize work and break intervals, receive wellness reminders, and open an immersive timer interface. It is most relevant for productivity, study, and habit-building workflows where local focus history and desktop focus controls are acceptable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run a local FastAPI server and expose local control endpoints. <br>
Mitigation: Run it only in a trusted local environment and review the exposed endpoints before enabling routine use. <br>
Risk: The skill can change desktop UI state and create launcher files. <br>
Mitigation: Disable desktop-control and shortcut-creation behavior unless those actions are expected for the deployment. <br>
Risk: The skill includes remote UI fallback behavior. <br>
Mitigation: Review the remote UI URL and disable remote loading if only local assets should be used. <br>
Risk: The self-repair automation may inspect or modify the skill's own files. <br>
Mitigation: Review and disable the self-repair patrol unless automated local repair is explicitly desired. <br>
Risk: The skill stores focus history and related user data locally. <br>
Mitigation: Confirm local storage location, retention, and backup behavior before use with sensitive productivity data. <br>


## Reference(s): <br>
- [Flow Immersion ClawHub page](https://clawhub.ai/zxj2devs/skills/flow-immersion) <br>
- [zxj2devs ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Remote immersive UI fallback](https://gpt.cntaxs.com/stustar-api/zhx/flow-Im.html) <br>
- [Local FastAPI interface](http://localhost:8765) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, API Calls, Files] <br>
**Output Format:** [Markdown guidance with JSON configuration, local HTTP API calls, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local configuration, focus history, repair queue data, backups, and desktop launcher files during normal use.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

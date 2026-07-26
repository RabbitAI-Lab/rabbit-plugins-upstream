## Description: <br>
Automate punching time in/out on WPS Time / NetTime (wpstime.com NetTime), including setup, clock in/out, break and lunch actions, status checks, screenshots, and brief confirmations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dxh141130](https://clawhub.ai/user/dxh141130) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Employees who use WPS Time / NetTime can ask an agent to clock in, clock out, start or end breaks and lunch, or check current punch status. The skill runs a local Playwright flow with Keychain-stored credentials and reports the result with a screenshot. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use saved credentials to change real workplace timeclock records. <br>
Mitigation: Use explicit commands, require confirmation before punch actions, and run status checks when the current punch state is uncertain. <br>
Risk: Credential setup through chat can expose passwords in chat history or gateway logs. <br>
Mitigation: Prefer the local terminal setup flow that stores credentials in macOS Keychain and never echo passwords back to the user. <br>
Risk: Screenshots may reveal sensitive timeclock or workplace information. <br>
Mitigation: Avoid sharing screenshots in sensitive channels and review attachments before redistribution. <br>


## Reference(s): <br>
- [Punchclock Runbook](references/PUNCHCLOCK_RUNBOOK.md) <br>
- [WPS Time / NetTime Login](http://www.wpstime.com/NetTime/Login.asp) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with inline shell commands; runtime actions return JSON status and screenshot files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Screenshots may contain timeclock details and should be shared only in appropriate channels.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

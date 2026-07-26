## Description: <br>
Control Android devices via ADB with support for UI layout analysis and visual feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[staticai](https://clawhub.ai/user/staticai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and automation engineers use this skill to connect to Android devices, inspect UI hierarchy, capture screenshots, and run ADB command sequences for app interaction and verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ADB gives an agent direct control over an Android device, including taps, text entry, app launches, screenshots, and settings changes. <br>
Mitigation: Use the skill only with devices you control, review commands before sensitive actions, and revoke USB or wireless debugging access when finished. <br>
Risk: Screenshots and UI dumps can expose sensitive screen content or account information. <br>
Mitigation: Avoid running the skill on sensitive screens and review captured files before sharing or retaining them. <br>


## Reference(s): <br>
- [ADB Connection on ClawHub](https://clawhub.ai/staticai/skills/android-adb) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes ADB, uiautomator, screencap, tap, text input, keyevent, and swipe command examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

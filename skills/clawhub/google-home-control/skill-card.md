## Description: <br>
Control smart home devices (lights, TV, etc.) via the Google Assistant SDK. Use when the user wants to trigger home automation commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tvdofficial](https://clawhub.ai/user/tvdofficial) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users who configure Google Assistant SDK credentials use this skill to let an agent send text commands to linked smart home devices such as lights, TVs, and appliances. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can issue Google Assistant commands to real linked home devices through the user's Google account. <br>
Mitigation: Install only for accounts and devices where agent-issued commands are acceptable, and require confirmation for sensitive actions. <br>
Risk: Stored OAuth credentials can allow continued access to Google Assistant if exposed or no longer needed. <br>
Mitigation: Keep credentials protected, use the documented credential path or environment variable carefully, and revoke the OAuth credential when the skill is no longer used. <br>
Risk: The evidence reports broad home-device control without clear safety boundaries. <br>
Mitigation: Avoid connecting safety-sensitive devices such as locks, security systems, thermostats, or high-risk appliances unless additional policy controls are in place. <br>


## Reference(s): <br>
- [Google Home Control on ClawHub](https://clawhub.ai/tvdofficial/skills/google-home-control) <br>
- [Google Cloud Console](https://console.developers.google.com/) <br>
- [Google Assistant SDK OAuth Scope](https://www.googleapis.com/auth/assistant-sdk-prototype) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown setup guidance and plain-text script responses or device-action output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the user's Google OAuth credentials and sends text queries to the Google Assistant SDK.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

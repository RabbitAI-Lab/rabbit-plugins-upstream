## Description: <br>
Query Fitbit health data (activity, sleep, heart rate, weight) via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pb3975](https://clawhub.ai/user/pb3975) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to let an agent retrieve Fitbit activity, profile, and daily summary data after the user authorizes Fitbit access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses sensitive Fitbit health and profile data after authorization. <br>
Mitigation: Review requested Fitbit consent scopes, use it only in trusted agent sessions, and avoid sharing outputs in heavily logged or shared chats. <br>
Risk: OAuth tokens are stored locally for continued Fitbit API access. <br>
Mitigation: Keep the local token file private, run fitbit logout when access is no longer needed, and revoke the app in Fitbit if the device or workspace is no longer trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pb3975/skills/fitbit-health) <br>
- [Fitbit app registration](https://dev.fitbit.com/apps) <br>
- [Clawdbot](https://github.com/clawdbot/clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [CLI text output or JSON responses with setup and authentication commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a local fitbit CLI binary and user-authorized Fitbit OAuth access.] <br>

## Skill Version(s): <br>
0.1.1 (source: package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

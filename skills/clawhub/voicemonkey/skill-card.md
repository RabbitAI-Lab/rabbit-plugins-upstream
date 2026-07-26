## Description: <br>
Control Alexa devices via VoiceMonkey API v2 - make announcements, trigger routines, start flows, and display media. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jayakumark](https://clawhub.ai/user/jayakumark) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Alexa users use this skill to generate VoiceMonkey API examples and guidance for making announcements, triggering routines, starting flows, and sending media to Echo devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The VoiceMonkey token can control Alexa devices tied to the user's account. <br>
Mitigation: Install only when the agent is trusted with the token, prefer Authorization-header examples, avoid exposing tokens in URLs, shell history, or logs, and rotate the token if it is exposed. <br>
Risk: Announcements, routines, flows, websites, and media actions may be disruptive or unexpected when sent to Alexa devices. <br>
Mitigation: Require explicit user confirmation before triggering routines, flows, websites, media playback, or loud announcements. <br>


## Reference(s): <br>
- [VoiceMonkey skill page](https://clawhub.ai/jayakumark/skills/voicemonkey) <br>
- [VoiceMonkey](https://voicemonkey.io) <br>
- [VoiceMonkey Console](https://console.voicemonkey.io) <br>
- [VoiceMonkey API v2](https://api-v2.voicemonkey.io) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with curl examples, JSON request bodies, and setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VOICEMONKEY_TOKEN and VoiceMonkey device identifiers supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

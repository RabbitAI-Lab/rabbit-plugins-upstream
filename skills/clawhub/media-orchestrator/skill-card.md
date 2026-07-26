## Description: <br>
Unified skill for resolving, downloading, and delivering audio, video, and Spotify media to chat platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sieershafilone](https://clawhub.ai/user/sieershafilone) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to fulfill media requests from WhatsApp or Telegram by resolving a requested track or video, downloading it, and sending the resulting file or Spotify playback metadata through the configured chat channel. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads third-party media and sends files through configured chat accounts. <br>
Mitigation: Confirm the requested media, recipient, and appropriate rights before use. <br>
Risk: Downloaded media files and Spotify metadata are written to the OpenClaw workspace without evidence of automatic deletion or retention limits. <br>
Mitigation: Clean the workspace periodically and avoid using the skill for sensitive or unnecessary media requests. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Text, Configuration instructions] <br>
**Output Format:** [Downloaded media files, JSON Spotify metadata, and chat status messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes media to the OpenClaw workspace and delivers files through configured WhatsApp or Telegram channels.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

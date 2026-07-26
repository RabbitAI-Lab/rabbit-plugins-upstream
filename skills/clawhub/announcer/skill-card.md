## Description: <br>
Announce text throughout the house via AirPlay speakers using Airfoil + ElevenLabs TTS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and home-automation users use this skill to generate spoken announcements and play them across configured AirPlay speakers through Airfoil. It is intended for macOS environments with Airfoil, ffmpeg, Python 3, the ElevenLabs sibling skill, and an ElevenLabs API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Announcement text is sent for ElevenLabs TTS generation. <br>
Mitigation: Avoid announcing secrets or highly sensitive personal information. <br>
Risk: The skill controls Airfoil speakers on the user's Mac. <br>
Mitigation: Review the configured speaker list, exclusions, and volume before use. <br>
Risk: Announcements may play through unintended AirPlay speakers if configuration is stale. <br>
Mitigation: Use the speaker listing command and update the configuration before broadcasting. <br>


## Reference(s): <br>
- [Announcer ClawHub page](https://clawhub.ai/odrobnik/skills/announcer) <br>
- [Announcer setup instructions](artifact/SETUP.md) <br>
- [Announcer article](artifact/ARTICLE.md) <br>
- [Airfoil](https://rogueamoeba.com/airfoil/) <br>
- [ElevenLabs](https://elevenlabs.io) <br>
- [OpenClaw](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Audio, JSON] <br>
**Output Format:** [CLI text and optional JSON speaker inventory; generated announcement audio is played through Airfoil.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires macOS, Airfoil, python3, ffmpeg, ELEVENLABS_API_KEY, and the ElevenLabs sibling skill.] <br>

## Skill Version(s): <br>
1.2.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

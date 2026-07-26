## Description: <br>
Play music on YouTube through visible playwright-cli browser automation, including song, artist, genre, playlist, playback-control, ad-skip, and voice-transcription correction workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whodidthese](https://clawhub.ai/user/whodidthese) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent operators use this skill to play and control YouTube music in a visible browser session. It is suited for music requests such as specific songs, artist mixes, genre playlists, playback controls, ad skipping, and correction of voice-transcribed song or artist names. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent browser profiles can retain YouTube or Google login state and other browser session data on disk. <br>
Mitigation: Use a dedicated browser profile, avoid sensitive browsing in the session, grant operating-system permissions only to a trusted local playwright-cli installation, and close or delete profile data when persistent login state is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/whodidthese/skills/my-play-music-from-yt) <br>
- [Playwright CLI reference](references/playwright-ref.md) <br>
- [YouTube result identification](references/youtube-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires playwright-cli and controls a visible persistent browser session.] <br>

## Skill Version(s): <br>
0.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

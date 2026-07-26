## Description: <br>
Control Devialet Phantom speakers via HTTP API for play/pause, volume control, mute/unmute, source selection, and speaker status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jgm2025](https://clawhub.ai/user/jgm2025) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to control Devialet Phantom, Mania, Reactor, and Dialog speakers on a trusted local network, with optional Spotify playback integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control Devialet speaker playback and Spotify playback. <br>
Mitigation: Install only when you are comfortable granting that control, and use the correct speaker IP on a trusted local network. <br>
Risk: Spotify credential and token files are stored locally for API-based playback. <br>
Mitigation: Keep those files private, limit filesystem access to them, and revoke the Spotify app token when it is no longer needed. <br>
Risk: Search-based playback can use desktop keystroke automation. <br>
Mitigation: Prefer direct Spotify URIs or API-based playback when possible, and review behavior before using search automation. <br>


## Reference(s): <br>
- [Devialet HTTP API Reference](references/api.md) <br>
- [ClawHub Devialet Speaker Control Release](https://clawhub.ai/jgm2025/skills/devialet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local speaker IP settings, Spotify desktop controls, and Spotify API authentication files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

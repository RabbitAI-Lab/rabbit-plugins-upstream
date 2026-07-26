## Description: <br>
Claw Desktop Pet helps an OpenClaw agent appear as a small Electron desktop companion with expressions, voice, mood colors, and lyric-style message overlays. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kk43994](https://clawhub.ai/user/kk43994) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to set up a desktop companion that gives an agent visible presence, speech, expressions, and desktop lyric-style messages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on a live external GitHub project and npm dependencies rather than a pinned reviewed commit. <br>
Mitigation: Review the current project and dependency tree before running, and run it without administrator privileges where possible. <br>
Risk: Optional MiniMax voice cloning can create consent and misuse concerns. <br>
Mitigation: Enable voice cloning only deliberately, use approved voices, and get consent before using any cloned voice. <br>
Risk: Optional Feishu/Lark sync can expose workplace messages to the desktop companion workflow. <br>
Mitigation: Enable message sync only when approved for the workspace, and avoid syncing sensitive messages unless explicitly permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kk43994/skills/desktop-pet) <br>
- [Declared project homepage](https://github.com/kk43994/claw-desktop-pet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include setup steps for optional voice cloning and message-sync integrations.] <br>

## Skill Version(s): <br>
2.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

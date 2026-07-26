## Description: <br>
Control macOS GUI apps visually by taking screenshots, detecting text with OCR, clicking, scrolling, typing, and pressing keys. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kekejun](https://clawhub.ai/user/kekejun) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use mac-use to let an AI agent inspect and operate macOS GUI applications through a screenshot, OCR, act, and verify loop. It is useful when a task requires GUI interaction and a direct API is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad visibility into the Mac screen and control over mouse, keyboard, and AppleScript actions across arbitrary applications. <br>
Mitigation: Install only when that control is intended, avoid sensitive apps and screens, and require explicit human approval before actions that send, buy, delete, approve, or change account or security settings. <br>
Risk: Screenshots and element maps are written to temporary files under /tmp. <br>
Mitigation: Clear /tmp/mac_use*.png and /tmp/mac_use_elements.json after use, especially after workflows that displayed private or regulated information. <br>
Risk: The type command uses clipboard paste, which can expose typed content through the system clipboard. <br>
Mitigation: Do not type passwords, API keys, recovery codes, or other secrets through this tool. <br>


## Reference(s): <br>
- [ClawHub mac-use skill page](https://clawhub.ai/kekejun/skills/mac-use) <br>
- [OpenClaw project](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands; the helper script returns JSON and writes annotated screenshot files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [macOS only; requires python3, Screen Recording permission, Accessibility permission, and local temporary files under /tmp.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

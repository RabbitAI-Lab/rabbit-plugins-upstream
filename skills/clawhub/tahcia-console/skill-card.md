## Description: <br>
Automates real Chrome browser sessions on macOS through a CLI, Chrome extension, WebSocket session, and macOS input helper. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tahcia](https://clawhub.ai/user/tahcia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation agents use this skill to drive a user's real Chrome and macOS desktop with screenshots, OCR, accessibility-tree inspection, and command-based UI actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad control over Chrome and macOS can perform unintended desktop actions. <br>
Mitigation: Grant access only in environments where desktop control is acceptable, review proposed actions before execution, and stop sessions when automation is no longer needed. <br>
Risk: The skill references local credential files and external screenshot analysis. <br>
Mitigation: Do not allow the skill to read local API key files or send screenshots to third-party vision services unless that access is explicitly intended. <br>
Risk: Persistent self-editing, scheduled scripts, or file overwrites can change behavior over time. <br>
Mitigation: Block edits to the skill file, scheduled automation, and file overwrites unless each action is explicitly approved for the current task. <br>


## Reference(s): <br>
- [Tahcia Console](https://www.tahcia.com/console) <br>
- [Tahcia Commands](https://www.tahcia.com/commands) <br>
- [Tahcia CLI Repository](https://github.com/tahcia/cli) <br>
- [Tahcia Homebrew Tap](https://github.com/tahcia/homebrew-tahcia) <br>
- [ClawHub Skill Page](https://clawhub.ai/tahcia/skills/tahcia-console) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Tahcia command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces short action plans and command sequences for real browser and macOS interaction.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

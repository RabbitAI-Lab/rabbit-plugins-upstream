## Description: <br>
Switch between AI models dynamically to optimize costs and performance when users request mode changes, status checks, or mode setup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[serudda](https://clawhub.ai/user/serudda) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to map eco, balanced, smart, and max modes to model IDs, switch the active model, and check which mode is currently configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change OpenClaw's default model, which may affect other sessions, behavior, and costs. <br>
Mitigation: Use explicit mode phrases, run /modes status after switching, and review the selected model before using SMART or MAX modes. <br>
Risk: Ambiguous standalone words such as eco, smart, or max can trigger a mode switch. <br>
Mitigation: Confirm the intended mode before updating configuration when the user request is ambiguous. <br>
Risk: Writing to local OpenClaw configuration files can corrupt settings if JSON is invalid or unrelated settings are overwritten. <br>
Mitigation: Validate JSON before writing and update only the model field while preserving all other OpenClaw settings. <br>


## Reference(s): <br>
- [Switch Modes Skill Page](https://clawhub.ai/serudda/skills/switch-modes) <br>
- [Switch Modes Reference Guide](artifact/REFERENCE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local OpenClaw mode mapping and default model configuration files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Desktop automation via native OS accessibility trees using the agent-desktop CLI for observing and interacting with desktop applications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lahfir](https://clawhub.ai/user/lahfir) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to guide agents through desktop GUI observation, interaction, app lifecycle, window, clipboard, notification, wait, and session workflows. It is intended for real desktop automation tasks where the calling agent must inspect UI state and act through the agent-desktop CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad control of a user's real desktop through accessibility and screen recording permissions. <br>
Mitigation: Grant permissions only to trusted launchers and install the skill only when real desktop operation is intended. <br>
Risk: Desktop observation, screenshots, clipboard use, and trace artifacts may expose sensitive application data. <br>
Mitigation: Avoid running the skill around secrets or sensitive apps, use --no-trace or short-lived sessions when possible, and clean up ~/.agent-desktop sessions after use. <br>
Risk: High-impact physical or forced input can disrupt active applications. <br>
Mitigation: Use headed or forceful commands only when explicit physical interaction is intended and verify UI state before continuing. <br>


## Reference(s): <br>
- [Agent Desktop Skill](https://clawhub.ai/lahfir/skills/agent-desktop) <br>
- [Observation Commands](artifact/references/commands-observation.md) <br>
- [Interaction Commands](artifact/references/commands-interaction.md) <br>
- [System Commands](artifact/references/commands-system.md) <br>
- [Common Automation Workflows](artifact/references/workflows.md) <br>
- [macOS Platform](artifact/references/macos.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs guide an agent that invokes the separate agent-desktop CLI; command results are expected to use structured JSON envelopes.] <br>

## Skill Version(s): <br>
0.1.21 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

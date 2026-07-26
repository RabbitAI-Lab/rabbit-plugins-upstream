## Description: <br>
Activate "Sport Mode" for high-frequency monitoring (default 3m heartbeat) and auto-cleanup. Use when supervising intense tasks (Codex, builds, migrations). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[l1vein](https://clawhub.ai/user/l1vein) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to temporarily increase heartbeat frequency and place a monitoring task in HEARTBEAT.md for long-running builds, coding-agent supervision, migrations, and turn-based interactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can overwrite or clear HEARTBEAT.md while changing heartbeat behavior. <br>
Mitigation: Back up existing HEARTBEAT.md content and confirm the workspace target before enabling or disabling Sport Mode. <br>
Risk: A persistent high-frequency task can encourage unattended command execution or repeated monitoring. <br>
Mitigation: Use only trusted task text, require a clear stop condition, and disable Sport Mode when the monitored task is finished. <br>
Risk: Users who need interactive approval for every command may lose oversight if the task asks the agent to continue autonomously. <br>
Mitigation: Review the task before installation or activation and avoid autonomous task text when interactive approval is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/l1vein/skills/sport-mode) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write or clear HEARTBEAT.md and adjust OpenClaw heartbeat configuration when invoked.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

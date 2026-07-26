## Description: <br>
Pure PowerShell GDI+ screenshot tool for Windows that captures the primary screen to a PNG file with automatic scaling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sorpresaaaa](https://clawhub.ai/user/sorpresaaaa) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation agents use this skill on Windows to capture the visible primary screen as a local PNG for documentation, troubleshooting, or downstream media workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Screenshots can capture private or sensitive information visible on the Windows screen. <br>
Mitigation: Review the screen before running the skill, store outputs in an intended directory, and delete screenshots that contain private information. <br>
Risk: Captured files are saved locally and may persist longer than intended. <br>
Mitigation: Set OPENCLAW_MEDIA_DIR to a controlled storage location and apply normal file retention or cleanup practices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sorpresaaaa/skills/windows-screenshot) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with PowerShell command examples; runtime output is a PNG file path prefixed with MEDIA:] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates timestamped PNG screenshots in OPENCLAW_MEDIA_DIR or the default local OpenClaw media directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

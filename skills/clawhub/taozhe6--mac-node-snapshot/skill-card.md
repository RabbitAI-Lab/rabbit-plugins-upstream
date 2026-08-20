## Description: <br>
A robust, permission-friendly method to capture macOS screens via OpenClaw screen.record. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[taozhe6](https://clawhub.ai/user/taozhe6) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to capture a visible macOS screen through OpenClaw screen.record, extract a PNG frame, and attach the resulting image when a user asks for a screenshot or screen inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Screen captures may include sensitive visible windows or data. <br>
Mitigation: Hide sensitive windows before use and grant macOS Screen Recording permission intentionally. <br>
Risk: Temporary MP4 and PNG capture files may remain in the skill tmp folder. <br>
Mitigation: Review and remove temporary capture files after they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/taozhe6/skills/mac-node-snapshot) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and local MP4/PNG file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires OpenClaw screen recording access and ffmpeg; temporary capture files are written under the skill tmp folder.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

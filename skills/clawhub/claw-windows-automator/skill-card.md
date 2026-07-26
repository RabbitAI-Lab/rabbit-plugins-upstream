## Description: <br>
Claw Windows Automator helps agents run Windows desktop automation tasks such as opening CMD in a target directory, sending commands or BAT scripts, showing an interruptible overlay, switching input methods, and downloading the latest GitHub source ZIP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangminrui2022](https://clawhub.ai/user/wangminrui2022) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to automate Windows workflows that require visible desktop control, command execution in a chosen folder, BAT/script launch, or downloading the latest GitHub source archive. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run commands, open browsers, download code, and change Python packages on a Windows desktop. <br>
Mitigation: Use it only in an isolated environment and require explicit operator confirmation before command execution, downloads, or dependency changes. <br>
Risk: Server security guidance identifies automatic pip/setuptools changes as a review point. <br>
Mitigation: Review dependency modification behavior before installation and pin or preinstall required packages where possible. <br>
Risk: Server security guidance identifies an undocumented WeChat automation task. <br>
Mitigation: Disable or remove the WeChat task unless it is intentionally needed and has been reviewed for the target environment. <br>
Risk: Server security guidance identifies unvalidated URL handling. <br>
Mitigation: Restrict downloads to trusted GitHub repository URLs and validate the target URL before running the download task. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wangminrui2022/skills/claw-windows-automator) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/wangminrui2022) <br>
- [Artifact README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and task parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local Windows automation instructions that may open applications, run commands, download archives, and modify the Python environment.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

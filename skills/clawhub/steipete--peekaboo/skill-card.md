## Description: <br>
Capture and automate macOS UI with the Peekaboo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users on macOS use Peekaboo to inspect screens, identify UI targets, and automate app, window, input, clipboard, menu, and screenshot workflows through CLI commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can inspect screen and clipboard contents and drive macOS UI input, which can expose secrets or perform unintended actions. <br>
Mitigation: Install only when UI automation is intended; review commands before running them and avoid sensitive screens, clipboard contents, passwords, and account flows unless the workflow is trusted. <br>
Risk: Peekaboo requires macOS Screen Recording and Accessibility permissions, giving it broad ability to observe and control the local UI. <br>
Mitigation: Grant permissions only on trusted Macs and periodically review or revoke those permissions when automation is no longer needed. <br>


## Reference(s): <br>
- [Peekaboo homepage](https://peekaboo.boo) <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/peekaboo) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference JSON CLI output and image or screenshot files produced by Peekaboo commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

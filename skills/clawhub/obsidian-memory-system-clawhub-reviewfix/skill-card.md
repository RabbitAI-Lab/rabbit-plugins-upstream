## Description: <br>
Persistent memory system using Obsidian as local storage for daily work logs, task tracking, decision records, and cross-session context continuity for AI coding agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI coding-agent users use this skill to capture and recall project memory in a local Obsidian vault, including work logs, tasks, decisions, and context from prior sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release contacts api.ideaidea.com.cn, sends user question text during order creation, and verifies a local payment credential with the service. <br>
Mitigation: Review the disclosed network flow before installation, avoid sending sensitive question text, and confirm the requested network, credential, and filesystem permissions are acceptable. <br>
Risk: The packaged artifacts mostly implement payment verification and do not include concrete Obsidian memory functionality. <br>
Mitigation: Confirm the installed artifact provides the expected memory workflow before relying on it for project records or cross-session continuity. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jinyu12166/skills/obsidian-memory-system-clawhub-reviewfix) <br>
- [clawtip verification service](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command outputs and local Obsidian note content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires clawtip-skill for payment verification before service delivery.] <br>

## Skill Version(s): <br>
3.0.36 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

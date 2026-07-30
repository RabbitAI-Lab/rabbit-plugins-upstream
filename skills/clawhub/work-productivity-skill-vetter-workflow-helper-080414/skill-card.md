## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows for bug fixing, safety hardening, reliability improvements, and adjacent skill planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users, skill authors, maintainers, and teams use this skill to turn demand for Skill Vetter-style workflows into concise plans, checklists, analyses, code changes, or decision aids. It is intended for practical productivity work around safer setup, reliability, bug fixes, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate too often because of generic keywords and implicit invocation. <br>
Mitigation: Review the trigger terms before installation and narrow invocation policy where the host platform allows it. <br>
Risk: Workflow guidance could be applied without checking whether it fits the user's actual repository, security posture, or release process. <br>
Mitigation: Require users to state success criteria and validate generated plans, checklists, code, or commands against their local constraints before use. <br>


## Reference(s): <br>
- [ClawHub Skill Release](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-080414) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [GitHub skill demand signal](https://clawhub.ai/skills/github) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [Offline Enterprise update packages issue](https://github.com/enocperez-spec/POS-Printer-Emulator-ESC-POS/issues/37) <br>
- [Automatic configuration restore points issue](https://github.com/enocperez-spec/POS-Printer-Emulator-ESC-POS/issues/32) <br>
- [Pre-commit hooks feature request](https://github.com/harsharajkumar-273/Proofdesk/issues/74) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include reusable checklists, workflow steps, assumptions, validation notes, and remaining risks.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

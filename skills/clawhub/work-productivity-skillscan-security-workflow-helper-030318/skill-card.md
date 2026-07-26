## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agent users, developers, skill authors, maintainers, and teams use this skill to turn demand for SkillScan-style security and productivity workflows into actionable plans, checklists, code changes, and validation notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger language and implicit invocation may cause the skill to activate in unrelated conversations. <br>
Mitigation: Narrow trigger terms or disable implicit invocation so the skill activates only for explicit SkillScan-style workflow support. <br>
Risk: Generated plans, checklists, code changes, or configuration suggestions may affect security posture if applied without review. <br>
Mitigation: Review proposed changes against the stated success criteria and scan or test affected skill artifacts before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [ClawHub Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [ClawHub self-improving agent demand signal](https://clawhub.ai/skills/self-improving-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include assumptions, limits, validation notes, and follow-up risks when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

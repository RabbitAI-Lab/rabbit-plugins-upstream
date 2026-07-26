## Description: <br>
Helps agent users and skill authors turn SkillScan-style security and reliability needs into practical workflows, checklists, plans, code changes, and verification notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and agent users use this skill to plan and validate SkillScan-style security, bug-fix, hardening, and reliability workflows. It helps produce practical local workflows, checklists, decision aids, implementation support, and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording can cause the skill to appear for generic security or bug-fix prompts. <br>
Mitigation: Prefer explicit invocation when the user specifically wants SkillScan-style workflow, checklist, hardening, or reliability support. <br>
Risk: Workflow or checklist guidance could be applied without sufficient review for the user's environment. <br>
Mitigation: Validate outputs against the stated success criteria and review security-sensitive changes before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-120220) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Threat modeling demand signal](https://news.ycombinator.com/item?id=48972048) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, code snippets, shell commands, and checklist-style guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, and follow-up risks when useful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

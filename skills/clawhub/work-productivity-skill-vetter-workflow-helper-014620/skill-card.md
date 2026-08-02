## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create, fix, harden, and validate Skill Vetter-style workflows for ClawHub skill work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style demand into practical workflows, checklists, analysis, code changes, or decision support. It emphasizes clear requirements, local-hardware-friendly implementation, and validation against visible success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad implicit activation could cause the skill to run during unrelated security, GitHub, or bug-fix prompts. <br>
Mitigation: Narrow trigger phrases and disable or tightly constrain implicit invocation before broad deployment. <br>
Risk: Workflow or security guidance may be incorrect or too general for a specific repository or team process. <br>
Mitigation: Review outputs before acting, validate them against the stated success criteria, and scan skill changes before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-014620) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [GitHub demand signal](https://clawhub.ai/skills/github) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, checklists, code snippets, shell commands, or configuration depending on the user request] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a short verification note, assumptions, limits, and next steps when useful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams produce practical workflows, artifacts, checklists, analyses, or implementation support for vetting skills, fixing bugs, hardening setups, and improving reliability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style needs into repeatable local workflows for review, reliability improvement, setup hardening, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger keywords could cause the helper to activate for unrelated security, GitHub, or installation requests. <br>
Mitigation: Narrow triggers and examples before publication so the skill is invoked only for explicit Skill Vetter or skill-review workflow requests. <br>
Risk: Workflow outputs may include advice, checklists, code changes, or commands that are unsuitable for a user's specific repository or environment. <br>
Mitigation: Review generated outputs against the stated success criteria and inspect any proposed commands or code before applying them. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-140500) <br>
- [Publisher Profile](https://clawhub.ai/user/kyro-ma) <br>
- [Self-Improving Agent Demand Signal](https://clawhub.ai/skills/self-improving-agent) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [GitHub Skill Demand Signal](https://clawhub.ai/skills/github) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, templates, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, validation steps, remaining risks, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

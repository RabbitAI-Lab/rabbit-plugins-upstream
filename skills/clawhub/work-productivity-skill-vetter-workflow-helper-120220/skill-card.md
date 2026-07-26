## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical workflows, artifacts, checklists, analyses, or code changes for skill vetting, bug fixes, setup hardening, safety, and reliability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent users, skill authors, maintainers, and teams use this skill to turn Skill Vetter-style demand into actionable review workflows, checklists, implementation plans, and verification notes. It is intended for practical work on bug fixes, setup hardening, safety review, reliability improvements, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger keywords and implicit invocation could route unrelated security, GitHub, or bug-fix requests through this workflow helper. <br>
Mitigation: Narrow the trigger keywords or disable implicit invocation before installation when precise activation is required. <br>
Risk: The skill can produce workflow, code, shell command, or configuration guidance that may be unsuitable for a specific repository or operating environment. <br>
Mitigation: Review generated steps against the user's stated constraints and verify proposed code, commands, and configuration before applying them. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-120220) <br>
- [Popular ClawHub Skill Demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub Skill Demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [Ask HN: Threat Modeling for Terraform/IaC](https://news.ycombinator.com/item?id=48972048) <br>
- [Feature Request: Improve App Installation and Discoverability](https://github.com/JvSlice/Ultimate-Window-Engineer-Tool/issues/17) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, with code blocks or command snippets when implementation support is requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tailored artifacts, reusable checklists, workflows, assumptions, limits, and verification notes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

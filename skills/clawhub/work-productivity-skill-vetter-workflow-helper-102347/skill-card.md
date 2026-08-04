## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical Skill Vetter-style workflows for bug fixing, setup hardening, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn demand for Skill Vetter-style workflows into concise plans, checklists, analysis, code changes, or decision aids. It is intended for practical workflow support around skill vetting, safety hardening, bug fixing, reliability improvement, and adjacent skill creation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words may cause this skill to appear for general security, GitHub, or bug-fix requests where a narrower workflow would be better. <br>
Mitigation: Use explicit invocation for this workflow until the triggers are narrowed or the caller confirms the skill-vetting context. <br>
Risk: Workflow recommendations may be incomplete or overly general if the user provides little context. <br>
Mitigation: State assumptions, ask only for missing information that materially changes the output, and validate the result against the user's success criteria. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-102347) <br>
- [Requirement plan](references/requirement-plan.md) <br>
- [Popular ClawHub skill demand: Skill Vetter](https://clawhub.ai/skills/skill-vetter) <br>
- [Popular ClawHub skill demand: Github](https://clawhub.ai/skills/github) <br>
- [Popular ClawHub skill demand: SkillScan](https://clawhub.ai/skills/skillscan) <br>
- [GitHub issue demand signal](https://github.com/realproject7/agentgather/issues/78) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Analysis, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown, optionally with inline code blocks, shell commands, checklists, templates, or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include visible assumptions, limits, validation notes, and practical next steps when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

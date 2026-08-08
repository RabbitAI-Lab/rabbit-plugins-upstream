## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixing, setup hardening, safety review, reliability improvement, and adjacent skill design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, maintainers, skill authors, and agent teams use this skill to turn SkillScan-style security and reliability needs into concrete workflows, checklists, analysis, code changes, or decision support. It is intended for work-productivity tasks that benefit from explicit planning, local-hardware-friendly implementation, and validation against stated success criteria. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation terms may route ordinary security, workflow, or bug-fix prompts through this skill unexpectedly. <br>
Mitigation: Limit activation to explicit SkillScan or security-workflow requests, or disable implicit invocation in environments that auto-select skills. <br>
Risk: The skill can produce workflow, checklist, code, shell command, or configuration guidance that may affect security posture. <br>
Mitigation: Review generated changes and validation notes before applying them in production or shared environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [AI policies demand signal](https://news.ycombinator.com/item?id=49112835) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, configuration snippets, and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces tailored artifacts and validation notes for the user's current security or workflow task.] <br>

## Skill Version(s): <br>
0.20260730.234524 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

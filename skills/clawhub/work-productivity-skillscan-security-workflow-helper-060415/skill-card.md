## Description: <br>
Helps skill authors, maintainers, and teams create SkillScan-style security, reliability, and workflow checklists, plans, analyses, and implementation guidance for ClawHub skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, skill authors, maintainers, and teams use this skill to turn security, reliability, and workflow-hardening needs into practical plans, checklists, analysis, code guidance, or reusable decision support. It is especially suited to ClawHub SkillScan-style review and improvement workflows that should remain feasible on local hardware. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad automatic activation may route generic security or workflow requests into this helper when a narrower skill would be better. <br>
Mitigation: Prefer explicit invocation by skill name; maintainers should narrow or disable implicit invocation for stricter environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-060415) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Threat modeling discussion signal](https://news.ycombinator.com/item?id=48972048) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or structured text with optional code, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, reusable checklists, and follow-up risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

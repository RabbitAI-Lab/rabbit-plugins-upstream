## Description: <br>
Helps agent users, skill authors, maintainers, and teams create practical SkillScan-style workflows for bug fixing, security hardening, reliability improvement, and adjacent skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, skill authors, maintainers, and agent users use this skill to turn broad SkillScan-style security and productivity needs into concrete workflows, checklists, analyses, code changes, or decision support. It is intended for local-hardware-friendly planning and validation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can auto-activate on broad terms such as security, gate, every, must, pass, before, activate, or bug fix, which may affect unrelated conversations. <br>
Mitigation: Prefer explicit invocation by skill name or narrow SkillScan workflow phrasing, and consider disabling implicit invocation before deployment. <br>
Risk: As a workflow helper, it can produce security or reliability recommendations that may be incomplete for a specific environment. <br>
Mitigation: Review generated plans, checklists, scripts, and configuration changes against local requirements before use. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-110318) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Threat Modeling for Terraform/IaC Demand Signal](https://news.ycombinator.com/item?id=48972048) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with optional code, shell command, checklist, and configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should state assumptions, validation notes, remaining risks, and next steps when helpful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create SkillScan-style workflows for bug fixes, setup hardening, safety checks, reliability improvements, and adjacent skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn security, bug-fix, setup-hardening, reliability, and adjacent skill-development requests into practical workflows, checklists, automation outlines, or implementation support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and implicit invocation may cause the skill to influence unrelated security, bug-fix, or workflow requests. <br>
Mitigation: Review routing before installation; narrow trigger terms or disable implicit invocation when precise activation is required. <br>
Risk: Workflow guidance may affect security or reliability decisions if applied without review. <br>
Mitigation: Review generated checklists, scripts, configuration changes, and adjacent skills before deployment, and scan resulting artifacts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-skillscan-security-workflow-helper-100358) <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [SkillScan Demand Signal](https://clawhub.ai/skills/skillscan) <br>
- [Skill Vetter Demand Signal](https://clawhub.ai/skills/skill-vetter) <br>
- [Security Workflow Demand Signal](https://github.com/EffortlessMetrics/ripr-swarm/issues/2009) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with optional code blocks, shell commands, checklists, configuration snippets, and validation notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's immediate context and may include reusable workflow artifacts or decision aids.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

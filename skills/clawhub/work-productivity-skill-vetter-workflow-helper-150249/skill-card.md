## Description: <br>
Helps agent users and skill authors create practical Skill Vetter-style workflows for bug fixing, setup hardening, safety review, reliability improvement, and adjacent skill creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn skill-vetting and work-productivity requests into concrete workflows, checklists, analyses, code changes, or decision support with explicit success criteria and verification notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger terms can cause the skill to activate when a user intended a different security, GitHub, or bug-fix workflow. <br>
Mitigation: Prefer explicit invocation by skill name, or narrow the trigger list before publishing or installing. <br>
Risk: Generated workflows, checklists, or code-support guidance may not match a user's environment or success criteria. <br>
Mitigation: Review assumptions and validation notes before applying changes, especially for safety or reliability work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-skill-vetter-workflow-helper-150249) <br>
- [Requirement plan](artifact/references/requirement-plan.md) <br>
- [Skill Vetter demand signal](https://clawhub.ai/skills/skill-vetter) <br>
- [SkillScan demand signal](https://clawhub.ai/skills/skillscan) <br>
- [Context-size demand signal](https://github.com/co-l/openfox/issues/120) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code blocks, shell commands, checklists, templates, and verification notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are tailored to the user's request and may include reusable workflows or decision aids.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Documentation-as-Source-of-Truth workflow. Use when working with projects that use docs/ as the canonical source for definitions, rules, and tasks. Routes to specialized sub-skills for specific documentation types. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eduardou24](https://clawhub.ai/user/eduardou24) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and project teams use this skill to treat a docs/ folder as the canonical source for definitions, rules, and tasks. It helps agents navigate documentation structure, choose specialized OGT Docs sub-skills, initialize docs-first projects, and resolve code/documentation conflicts in favor of reviewed docs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outdated or incorrect project docs may steer agent work, because the skill instructs agents to resolve code/documentation conflicts in favor of documentation. <br>
Mitigation: Keep docs reviewed and current, and require human review before applying changes driven by documentation conflicts. <br>
Risk: Referenced OGT Docs sub-skills may introduce separate behavior or risk profiles. <br>
Mitigation: Review and scan each referenced sub-skill before relying on it. <br>


## Reference(s): <br>
- [OGT Docs ClawHub skill page](https://clawhub.ai/eduardou24/skills/ogt-docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with folder structures, tables, workflow diagrams, and task routing notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [None] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

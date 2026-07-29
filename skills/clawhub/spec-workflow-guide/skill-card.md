## Description: <br>
Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to decide when a change needs a requirements, design, and task-planning workflow before implementation. It helps make acceptance criteria explicit, preserve traceability, and avoid starting larger or ambiguous work before the user confirms the plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can slow larger changes by requiring explicit requirements, design, task planning, and user confirmation before implementation. <br>
Mitigation: Use it for medium-to-large, ambiguous, multi-module, or architecture-heavy work, and skip the full workflow for small, clear, low-risk changes as the skill itself directs. <br>
Risk: Overly vague requirements or tasks could lead to incorrect implementation plans. <br>
Mitigation: Keep acceptance criteria testable, use EARS-style criteria, and confirm each phase with the user before proceeding. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide) <br>
- [CloudBase main entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Current skill raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/spec-workflow/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, configuration] <br>
**Output Format:** [Markdown requirements, design, and task-plan documents with concise agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation before moving from requirements to design, from design to task planning, and from task planning to implementation.] <br>

## Skill Version(s): <br>
1.18.17 (source: ClawHub release metadata; artifact frontmatter reports 2.25.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

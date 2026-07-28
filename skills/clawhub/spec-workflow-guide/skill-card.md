## Description: <br>
Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when medium-to-large coding changes need requirements, design, and task planning before implementation. It guides agents through concise requirements, technical design, task breakdown, and user-confirmed execution for multi-module, UI-heavy, data-model, or architecture-heavy work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can slow larger coding requests by adding requirements, design, and task-confirmation phases. <br>
Mitigation: Apply the skill's decision rule: use the full workflow for medium or large unclear work, and skip it for small, low-risk, already precise changes. <br>
Risk: The skill may direct agents to consult published CloudBase sibling references for UI or data-model work. <br>
Mitigation: Review the referenced sibling skill content before relying on it for project-specific UI, data-model, or architecture decisions. <br>
Risk: Planning artifacts can encode incorrect acceptance criteria or technical assumptions if the original request is underspecified. <br>
Mitigation: Ask follow-up questions for core behavior, use EARS-style acceptance criteria, and require user confirmation before moving from requirements to design, tasks, and execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide) <br>
- [CloudBase main entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Spec workflow raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/spec-workflow/SKILL.md) <br>
- [UI design sibling reference](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md) <br>
- [Data model creation sibling reference](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/data-model-creation/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown documents and concise agent guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When the full workflow is used, the skill produces requirements.md, design.md, and tasks.md under specs/<spec_name>/ before implementation.] <br>

## Skill Version(s): <br>
1.18.15 (source: server release metadata; artifact frontmatter says 2.24.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

## Description: <br>
Guides agents through requirements, technical design, and task planning before medium-to-large coding changes, especially when work spans modules or acceptance criteria are unclear. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to have an agent clarify requirements, document design decisions, and prepare implementation tasks before starting substantial or ambiguous coding work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can slow larger tasks by requiring requirements, design, and task confirmation before coding. <br>
Mitigation: Apply it to medium-to-large or unclear work, and skip the full workflow for small, low-risk changes with clear acceptance criteria. <br>
Risk: Planning documents can capture incorrect scope when the request is underspecified. <br>
Mitigation: Ask follow-up questions for core product behavior and require confirmation before moving from requirements to design, tasks, and execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide) <br>
- [CloudBase main entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Spec workflow raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/spec-workflow/SKILL.md) <br>
- [UI design sibling reference](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md) <br>
- [Data model sibling reference](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/data-model-creation/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown planning documents and implementation checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce requirements.md, design.md, and tasks.md under a specs directory before implementation.] <br>

## Skill Version(s): <br>
1.18.14 (source: ClawHub release evidence; artifact frontmatter reports 2.24.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

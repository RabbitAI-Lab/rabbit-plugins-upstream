## Description: <br>
Use when medium-to-large changes need explicit requirements, technical design, and task planning before implementation, especially for multi-module work, unclear acceptance criteria, or architecture-heavy requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to decide when a medium-to-large software change needs a staged requirements, design, and task workflow. It guides creation of traceable Markdown spec files before implementation begins. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can add planning overhead to small or already precise requests. <br>
Mitigation: Use the documented decision rule to skip the full workflow for small, low-risk tasks with clear acceptance criteria. <br>
Risk: The skill creates visible spec files in the workspace. <br>
Mitigation: Review the generated requirements, design, and task files before implementation begins. <br>
Risk: External fallback links are included for related CloudBase skills. <br>
Mitigation: Treat fallback links as documentation references, not automatic execution steps. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/spec-workflow-guide) <br>
- [CloudBase main entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Spec workflow raw source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/spec-workflow/SKILL.md) <br>
- [UI design sibling skill](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md) <br>
- [Data model creation sibling skill](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/data-model-creation/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance] <br>
**Output Format:** [Markdown files and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates specs/<spec_name>/requirements.md, specs/<spec_name>/design.md, and specs/<spec_name>/tasks.md; implementation starts only after task-plan confirmation.] <br>

## Skill Version(s): <br>
1.18.20 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

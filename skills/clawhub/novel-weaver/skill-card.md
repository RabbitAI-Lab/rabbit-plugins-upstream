## Description: <br>
novel-weaver helps agents plan, draft, and validate structured long-form fiction with outline, causality, continuity, style, logic, fidelity, ending, entity, and character-alias checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and writing-focused agents use novel-weaver to plan, draft, and validate long-form fiction through staged outline confirmation, chapter/substructure writing, continuity checks, and ending/fidelity review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional model setup can install third-party packages and download models, including a Transformers load path that enables trust_remote_code=True. <br>
Mitigation: Review and approve optional installation commands separately; use trusted package indexes and model sources, and avoid trust_remote_code unless the model code has been reviewed. <br>
Risk: The skill is a local, stateful novel-project manager that stores project data and model caches on disk. <br>
Mitigation: Confirm data and cache locations before use, keep generated files within the expected skill data directory, and avoid storing sensitive manuscript content unless local storage is acceptable. <br>
Risk: Generic writing prompts may trigger the workflow when the user intended a smaller editing or answer task. <br>
Mitigation: Check trigger fit before activation and decline the workflow for translation, proofreading, brief-answer, presentation, drawing, or unrelated requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/novel-weaver) <br>
- [Execution standards](references/execution_standards.md) <br>
- [Workflow hooks](references/hooks.md) <br>
- [Examples](references/examples.md) <br>
- [FAQ](references/faq.md) <br>
- [Permissions](references/permissions.md) <br>
- [Changelog](references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON state, and plain-text fiction drafts and reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create and update local project state, chapter text, reports, and optional local model caches.] <br>

## Skill Version(s): <br>
1.35.4 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

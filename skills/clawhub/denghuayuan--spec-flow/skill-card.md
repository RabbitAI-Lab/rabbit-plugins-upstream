## Description: <br>
Spec Flow helps an agent turn a feature idea or product request into a lightweight Chinese-language specification-driven development workflow with constitution, spec, plan, and tasks documents under a .specify directory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[denghuayuan](https://clawhub.ai/user/denghuayuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use Spec Flow before implementation to clarify what to build, why it matters, how it should be implemented, and which tasks should be completed. The workflow is intended for single-flow development planning and explicitly does not implement code by itself. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local project structure and context to generate planning documents, which may capture sensitive internal architecture or project details. <br>
Mitigation: Review generated .specify documents before sharing or committing them, and remove sensitive details that should not leave the project. <br>
Risk: The skill writes .specify planning files and may produce inaccurate constraints or plans when repository context is incomplete. <br>
Mitigation: Use the built-in review pauses for constitution, spec, and plan stages, and run the analyze checklist before generating tasks for medium- or high-risk changes. <br>
Risk: The skill is intended for Chinese-language output, which may not fit teams that require another language. <br>
Mitigation: Adapt the templates or explicitly override the desired language before using the workflow. <br>


## Reference(s): <br>
- [Analyze checklist](references/analyze-checklist.md) <br>
- [Constitution template](references/constitution-template.md) <br>
- [Specification template](references/spec-template.md) <br>
- [Plan template](references/plan-template.md) <br>
- [Tasks template](references/tasks-template.md) <br>
- [ClawHub skill page](https://clawhub.ai/denghuayuan/skills/spec-flow) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Markdown planning documents written to .specify paths, plus concise review summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces Chinese-language constitution, spec, plan, and tasks documents; pauses for user review at key stages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

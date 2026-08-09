## Description: <br>
Use when writing any generative prompt - ritual seed, explicit structure, scenario axes, and quality gates before paid API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and creative agents use this skill to structure generative media prompts, rotate scenario axes, and run approval and quality gates before spending generation credits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Companion generation skills may spend API credits or upload assets when approval gates are bypassed. <br>
Mitigation: Keep clarification and approval gates enabled unless the user explicitly opts into automation. <br>
Risk: Generated media prompts can drift from locked brand, subject, format, or safety constraints. <br>
Mitigation: Use brief locks, explicit prompt structure, and quality checklists before advancing to paid or downstream steps. <br>


## Reference(s): <br>
- [Generation diversity guide](references/generation-diversity.md) <br>
- [Clarification intake](references/clarification-intake.md) <br>
- [Still-image prompt flow](references/still-image-prompt-flow.md) <br>
- [Generation quality checklist hub](references/generation-quality-checklists.md) <br>
- [Workflow feedback gates](references/workflow-feedback-gates.md) <br>
- [String Seed of Thought](https://pub.sakana.ai/ssot/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with prompt drafts, checklists, and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires approval gates before paid generation unless explicitly waived.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

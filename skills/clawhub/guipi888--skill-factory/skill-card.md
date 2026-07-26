## Description: <br>
Skill Factory helps agents create, update, validate, and publish ClawHub-style skills through overlap review, safety checks, SKILL.md authoring, and publishing guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[guipi888](https://clawhub.ai/user/guipi888) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and skill authors use this skill to create or upgrade agent skills, compare proposed skills against an existing skill library, run a basic safety review, and prepare publication steps for Xiaping, GitHub, and ClawHub. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change local skill files as part of create or upgrade workflows. <br>
Mitigation: Review proposed file edits before applying them, and run validation before deploying or publishing a generated skill. <br>
Risk: The skill includes publishing workflows for external services. <br>
Mitigation: Require explicit user confirmation before publishing to Xiaping, GitHub, or ClawHub. <br>
Risk: Broad trigger terms may route unrelated AI, tool, creation, or publishing requests into a high-impact workflow. <br>
Mitigation: Narrow activation triggers or confirm intent before invoking the skill for ordinary AI/tool requests. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/guipi888/skill-factory) <br>
- [Output Patterns](references/output-patterns.md) <br>
- [Workflow Patterns](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline code blocks and structured checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or generate SKILL.md content, validation reports, release steps, and publishing commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

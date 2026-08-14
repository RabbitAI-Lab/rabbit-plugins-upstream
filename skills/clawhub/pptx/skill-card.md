## Description:

Create, edit, and analyze PowerPoint presentations. Invoke when user asks about PPT, slides, presentations, or needs to create/modify .pptx files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xztzmr](https://clawhub.ai/user/xztzmr)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external users use this skill to create, edit, analyze, and QA PowerPoint presentations when working with slides or .pptx files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad slide or presentation-design prompts and inspect or modify unintended files.

Mitigation: Only provide presentations and templates intended for the task; review file paths and generated changes before execution.

Risk: Generated presentations can contain layout, contrast, or content errors.

Mitigation: Run content and visual QA with text extraction and thumbnails before using or sharing output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xztzmr/skills/pptx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Files]

**Output Format:** [Markdown guidance with inline shell commands and code; generated or modified .pptx files when the agent applies the workflow.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes content and visual QA guidance for presentation outputs.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

SurgeonEdit applies minimal, tone-preserving edits to existing Chinese or English text while preserving structure, length, emphasis, and formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tianzhiceng297-boop](https://clawhub.ai/user/tianzhiceng297-boop)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to revise, correct, delete, soften, reword, or adjust a specific part of an existing Chinese or English document without expanding or visibly marking the change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may pass sensitive before-and-after text or file paths to the optional local audit script.

Mitigation: Run the audit locally and only point it at documents intended for processing.

## Reference(s):

- [Minimal Edit Examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands]

**Output Format:** [Clean revised text, with optional Markdown or shell commands for local audit checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed to return only the revised text unless the user asks for explanation.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

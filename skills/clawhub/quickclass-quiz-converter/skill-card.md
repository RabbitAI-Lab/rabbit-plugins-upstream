## Description:

Convert learning materials from Word, PDF, and images into QuickClass quiz JSON for single-choice, multiple-choice, and true/false classroom assignments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[makerguan](https://clawhub.ai/user/makerguan)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers, curriculum authors, and education tool operators use this skill to turn source teaching materials into QuickClass-compatible quiz JSON, with optional supporting Word documents for image-based questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes teaching materials that may include images, answer keys, copyrighted content, or student-related information.

Mitigation: Use it only with materials you are allowed to process, and confirm where OCR and image-understanding tools run before using scanned-PDF or image workflows.

Risk: OCR or image-understanding steps can misread question text, answer choices, diagrams, or answer keys.

Mitigation: Review the extracted intermediate JSON, verify mapped images and answers, and validate the final QuickClass file before import.

## Reference(s):

- [QuickClass Schema Specification](artifact/references/quickclass_schema.md)
- [ClawHub Skill Page](https://clawhub.ai/makerguan/skills/quickclass-quiz-converter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and generated JSON or Word output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces QuickClass quiz JSON and, when source questions include images, an optional companion Word document with image references.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

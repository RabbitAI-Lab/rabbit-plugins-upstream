## Description:

Systematically learn, study, or analyze any subject from first principles and produce a structured learning document the user can read and review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Learners, developers, and engineers use this skill to understand a subject from its fundamentals and create a structured learning document for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running examples from an unfamiliar repository may execute code without adequate safeguards.

Mitigation: Inspect the code first, require approval before running examples, and use a disposable sandbox without credentials and with restricted filesystem and network access.

Risk: The document scaffold overwrites an existing file at the chosen output path.

Mitigation: Choose a new output filename before creating the scaffold.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/fize/skills/first-principles)
- [Learning document template](references/document-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown learning document]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Self-contained content tailored to the subject being studied.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

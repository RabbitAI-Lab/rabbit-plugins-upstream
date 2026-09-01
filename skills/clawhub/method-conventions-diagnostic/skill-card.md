## Description:

Diagnoses academic convention issues in psychology Method sections, including citation attribution, ethics statements, transparency reporting, and terminology or formatting consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjinhongmy-pixel](https://clawhub.ai/user/wangjinhongmy-pixel)

### License/Terms of Use:

MIT-0

## Use Case:

Academic writers, reviewers, and research-support agents use this skill to evaluate psychology empirical Method sections for clear citation attribution, accurate adapted-method labeling, ethics and TOP/JARS transparency, and consistent terminology and formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact references local Windows paths and an external textbook PDF that may not exist in the deployment environment.

Mitigation: Treat the bundled checklist, rubric, and examples as the available operating evidence unless the external textbook source is separately provided and verified.

Risk: The skill processes manuscript text that may contain unpublished research details or participant-sensitive information.

Mitigation: Provide only the manuscript content needed for diagnosis and redact confidential or identifying details when the execution environment is not approved for that data.

Risk: Academic convention findings can vary by target journal and may be incomplete when the manuscript lacks context such as IRB status, preregistration links, or supplement availability.

Mitigation: Have a domain reviewer compare the output against the target journal guide, ethics records, preregistration materials, and data or code availability statements before submission.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Academic conventions checklist](artifact/references/checklist.md)
- [Academic conventions scoring rubric](artifact/references/rubric.md)
- [Bundled positive examples](artifact/references/examples/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown diagnostic report with scores, issue flags, revision guidance, and positive example references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled markdown checklist, rubric, and example references; no hidden execution is described in the security evidence.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

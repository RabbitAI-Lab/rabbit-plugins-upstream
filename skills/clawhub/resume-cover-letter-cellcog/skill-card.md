## Description:

Resume helps agents create ATS-optimized resumes, CVs, cover letters, LinkedIn profiles, and other career documents with CellCog's research-first workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cellcog](https://clawhub.ai/user/cellcog)

### License/Terms of Use:

MIT-0

## Use Case:

External users, job seekers, and agents use this skill to prepare tailored resumes, CVs, cover letters, LinkedIn profile copy, and portfolio documents for specific roles or companies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume, cover-letter, and career-history prompts may include sensitive personal information and may be sent to CellCog for processing.

Mitigation: Include only necessary details, avoid unnecessary sensitive information, and review CellCog's data-handling terms before using real personal documents.

Risk: The skill requires CELLCOG_API_KEY, so exposed credentials could affect account access or usage.

Mitigation: Store the API key in a secure environment variable or secret manager and do not commit it to prompts, files, or logs.

Risk: Generated resumes, cover letters, or profile copy can become misleading if the prompt lacks accurate supporting details.

Mitigation: Review generated documents before use and keep claimed achievements, metrics, and experience grounded in supplied career history.

## Reference(s):

- [CellCog homepage](https://cellcog.ai)
- [ClawHub Resume skill page](https://clawhub.ai/cellcog/skills/resume-cover-letter-cellcog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with Python snippets and generated career document content or files such as PDF and DOCX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and CELLCOG_API_KEY; resume, cover-letter, and career-history prompts may be sent to CellCog for processing.]

## Skill Version(s):

1.0.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

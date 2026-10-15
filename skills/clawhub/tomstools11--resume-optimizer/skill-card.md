## Description:

Resume Optimizer helps agents create, tailor, analyze, and export ATS-friendly resumes in chronological, functional, or combination formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomstools11](https://clawhub.ai/user/tomstools11)

### License/Terms of Use:


## Use Case:

External users and agents use this skill to build new resumes, tailor existing resumes to job descriptions, review resumes for improvement opportunities, and generate ATS-friendly PDF outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The PDF generation script can install an unpinned reportlab package into the active Python environment at runtime.

Mitigation: Run PDF generation in a disposable virtual environment or container, or preinstall a pinned reportlab dependency and remove the runtime install path before deployment.

Risk: Resume content and generated filenames can contain personal information.

Mitigation: Ask users to include only necessary resume details, avoid unrelated sensitive data, and review output filenames before sharing generated PDFs.

## Reference(s):

- [Resume Optimizer release page](https://clawhub.ai/tomstools11/skills/resume-optimizer)
- [Resume Best Practices](references/best-practices.md)
- [ATS Optimization Guide](references/ats-optimization.md)
- [Resume Templates](references/templates.md)
- [Resume Analysis Checklist](references/analysis-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, files, guidance]

**Output Format:** [Markdown guidance, structured resume content, Python-assisted PDF files, and shell commands for PDF generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated resumes may include personal information and are expected to be saved as downloadable PDF files when export is requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

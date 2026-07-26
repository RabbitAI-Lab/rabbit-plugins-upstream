## Description: <br>
Professional resume builder with PDF export, ATS optimization, and analysis capabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomstools11](https://clawhub.ai/user/tomstools11) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to create, tailor, analyze, and export ATS-friendly resumes for specific roles. It supports chronological, functional, and combination resume formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The PDF generator can automatically install an unpinned Python package into the host environment. <br>
Mitigation: Run PDF export in a virtual environment or install ReportLab through a trusted dependency process before using the generator. <br>
Risk: Resume content can contain personal information. <br>
Mitigation: Handle generated resumes as sensitive files and remove exported files when they are no longer needed. <br>


## Reference(s): <br>
- [Resume Analysis Checklist](references/analysis-checklist.md) <br>
- [ATS Optimization Guide](references/ats-optimization.md) <br>
- [Resume Best Practices](references/best-practices.md) <br>
- [Resume Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance, JSON resume content, Python shell commands, and PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated PDFs are intended to be ATS-friendly and downloadable by the user.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

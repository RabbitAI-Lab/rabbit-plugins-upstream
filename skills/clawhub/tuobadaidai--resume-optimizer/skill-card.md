## Description: <br>
Resume Optimizer evaluates and rewrites user-provided resumes against optional job descriptions, produces before/after scoring reports, and exports ATS-compatible DOCX/PDF resume files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Job seekers and career-support agents use this skill to assess resumes, align them to optional job descriptions, rewrite experience using STAR-style evidence, and prepare ATS-friendly export files without inventing claims. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume and job-description inputs can contain sensitive personal or employment information. <br>
Mitigation: Redact unnecessary sensitive details before use and share only the information needed for the optimization task. <br>
Risk: Generated DOCX/PDF resume exports remain on disk after the workflow completes. <br>
Mitigation: Choose the output directory deliberately, review generated files, and remove local copies that are no longer needed. <br>
Risk: PDF export depends on local conversion tooling and Python dependencies. <br>
Mitigation: For higher-assurance environments, pin dependencies and use a trusted absolute LibreOffice path before enabling PDF conversion. <br>


## Reference(s): <br>
- [ATS Compatibility Optimization Guide](references/ats-optimization.md) <br>
- [JD Tailoring Method](references/jd-tailoring.md) <br>
- [STAR Methodology and Strong Verb Library](references/star-methodology.md) <br>
- [Edge Cases and Fault Tolerance](references/edge-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, guidance] <br>
**Output Format:** [Markdown reports and resume drafts, with optional DOCX/PDF files generated from Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided resume and job-description content; DOCX/PDF export writes files to a chosen output directory.] <br>

## Skill Version(s): <br>
1.5.1 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

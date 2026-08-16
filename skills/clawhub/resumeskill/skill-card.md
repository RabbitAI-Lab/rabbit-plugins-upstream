## Description:

Resume Tailor helps job seekers research a target role, rewrite a truthful resume for that role, and prepare interview materials from the revised resume.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qingjiu061](https://clawhub.ai/user/qingjiu061)

### License/Terms of Use:

MIT-0

## Use Case:

External job seekers and career-preparation agents use this skill to turn a resume, target company, target role, and job description into role research, a tailored resume draft, and interview preparation materials. The workflow is intended for internship, campus recruiting, and experienced-hire preparation while keeping user confirmation before major rewrite and interview-script steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes resumes and job materials that may contain sensitive personal data.

Mitigation: Use it only when the user is comfortable sharing those materials with the agent, and avoid adding unnecessary private details.

Risk: Resume rewrites and interview scripts could overstate claims, metrics, titles, or ownership.

Mitigation: Review every rewritten statement before use and keep claims grounded in the user's real experience.

Risk: The included DOCX generator depends on python-docx when producing Word output.

Mitigation: Run the generator in a controlled environment and consider pinning python-docx before executing it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qingjiu061/skills/resumeskill)
- [Resume rewriting playbook](artifact/resume-playbook.md)
- [Interview preparation playbook](artifact/interview-playbook.md)
- [Resume DOCX generator](artifact/generate_resume.py)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, guidance]

**Output Format:** [Markdown reports, resume text or DOCX files, and concise user-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate role research, a tailored resume document, interview scripts, and a resume risk map; DOCX generation depends on python-docx.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

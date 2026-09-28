## Description:

Creates tailored CVs, cover letters, and plain-text applications from structured profile and job data, with optional local PDF rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawjames1](https://clawhub.ai/user/clawjames1)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers use this skill to draft role-specific application documents from their own profile and a job description, then review the materials before any submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private profile and application details may be exposed if stored in the installed skill or shared without approval.

Mitigation: Keep real profiles and generated applications in private directories outside the skill, and obtain destination-specific approval before sending them.

Risk: Application materials may contain inaccurate or unsupported claims.

Mitigation: Check all qualifications and employment claims against the user's profile and review each document before use.

Risk: Rendering untrusted LaTeX source may be unsafe.

Mitigation: Render PDFs only from generated or trusted .tex files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clawjames1/skills/job-application)
- [Usage and setup guide](artifact/README.en.md)
- [Application generation specification](artifact/openspec/specs/application-generation/spec.md)
- [Persistent data specification](artifact/openspec/specs/persistent-data/spec.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Plain text, LaTeX source, and optional PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PDF rendering requires pdflatex; applications are not submitted automatically.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

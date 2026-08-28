## Description:

Creates fact-grounded Reactive Resume JSON or offline-ready single-file HTML resumes from user-provided or approved facts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xcjl](https://clawhub.ai/user/0xcjl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create or improve professional resumes as importable Reactive Resume JSON, standalone HTML resumes, or both. It supports bilingual resume workflows, print-friendly HTML, and explicitly authorized static deployment checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume outputs may contain personal data such as contact details, work history, education, and links.

Mitigation: Review generated resumes before sharing and remove details that should not become public.

Risk: Deployment or application-tracking actions can publish personal information or change connected records.

Mitigation: Proceed only after explicit authorization and confirm which contact details may be public before publishing or changing records.

Risk: Polished resume language can imply unsupported experience, dates, metrics, credentials, or outcomes.

Mitigation: Use only user-provided or explicitly approved facts and ask clarification questions when information is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/0xcjl/skills/resume-creator)
- [Reactive Resume](https://rxresu.me/)
- [Reactive Resume schema](https://rxresu.me/schema.json)
- [Reactive Resume Schema Reference](references/schema.md)
- [Presentation Selection](references/template-selection.md)
- [HTML Resume Quality Check](references/html-quality-check.md)
- [HTML Resume Styles](references/html-styles.md)
- [Application Tracking](references/application-tracking.md)
- [Reactive Resume project](https://github.com/AmruthPillai/Reactive-Resume)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Reactive Resume JSON, self-contained HTML, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated resumes should use only user-provided or approved facts; HTML output is self-contained and deployment is explicit opt-in.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

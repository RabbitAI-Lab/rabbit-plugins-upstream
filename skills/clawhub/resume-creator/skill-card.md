## Description:

Create, make, write, or improve a resume; output valid Reactive Resume JSON or a standalone, deployable single-file HTML resume.

This skill is ready for commercial/non-commercial use.

## Publisher:

[0xcjl](https://clawhub.ai/user/0xcjl)

### License/Terms of Use:

MIT

## Use Case:

External users, job seekers, and agents use this skill to collect verified resume facts and generate importable Reactive Resume JSON, offline-ready HTML resumes, or both.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume outputs may include personal contact details that become public if shared or deployed.

Mitigation: Review generated content and confirm publication intent before sharing or authorizing deployment.

Risk: Polished resume prose can overstate unsupported claims when source facts are incomplete.

Mitigation: Use only user-provided or explicitly approved facts, and ask targeted follow-up questions for missing details.

Risk: Optional deployment and job-application tracking paths can publish or mutate data when intentionally authorized.

Mitigation: Use those paths only after explicit user authorization and verify the target content or record before taking action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/0xcjl/skills/resume-creator)
- [Reactive Resume](https://rxresu.me/)
- [Reactive Resume Schema](https://rxresu.me/schema.json)
- [Reactive Resume Schema Reference](references/schema.md)
- [Presentation Selection](references/template-selection.md)
- [HTML Resume Styles](references/html-styles.md)
- [HTML Resume Quality Check](references/html-quality-check.md)
- [Application Tracking](references/application-tracking.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Reactive Resume JSON, Markdown guidance, or standalone single-file HTML]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a self-contained HTML resume with inline CSS or schema-valid JSON from user-provided and approved resume facts.]

## Skill Version(s):

1.0.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

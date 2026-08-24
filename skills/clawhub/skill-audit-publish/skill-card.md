## Description:

Audit-first pipeline that helps an agent sanitize, transform, verify, publish, and install-check an OpenClaw skill for ClawHub without leaking personal data, credentials, or model-specific references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this skill to prepare an OpenClaw skill for ClawHub release through sanitization, transformation, verification, publishing, and install-check steps. It is intended for public skill publishing workflows where personal data, credentials, model-specific references, and incorrect release metadata must be reviewed before upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing may expose personal data, credentials, model-specific references, internal paths, or unsafe patterns if the audit is skipped.

Mitigation: Run the sanitization checklist and have the user review every kept-with-reason item before approving publication.

Risk: Patch or repeat-publish shortcuts can reduce review of public content changes.

Mitigation: Review the generated publish folder and approval message carefully, especially for meaningful content or metadata changes.

Risk: Wrong slugs or nested source folders can publish the wrong package or make installs ambiguous.

Mitigation: Pass the canonical slug explicitly and verify that SKILL.md is at the publish root before running the publish command.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/skill-audit-publish)
- [sanitize.md](sanitize.md)
- [transform.md](transform.md)
- [verify.md](verify.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a publish folder and an approval message before any publish command is run.]

## Skill Version(s):

1.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

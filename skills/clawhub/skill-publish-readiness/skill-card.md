## Description:

Reviews ClawHub skill and plugin release candidates before publication for missing files, version inconsistencies, environment declaration gaps, security risks, and weak differentiation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill to perform a pre-publication self-review before releasing ClawHub skills or plugins. It produces a release-readiness verdict with blockers, risks, a shortest fix path, differentiation scoring, and next-step validation or dry-run commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect local skill or plugin files and suggest ClawHub validation, dry-run, or publish commands.

Mitigation: Run validation and dry-run commands before publication, and review any suggested publish command before execution, especially commands without --dry-run.

Risk: Publish-readiness guidance may be incomplete or need adjustment for a specific release.

Mitigation: Use the report as review guidance and confirm blockers, metadata, license terms, and security findings before publishing.

## Reference(s):

- [Project Homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [Consistency Rules](artifact/references/consistency_rules.md)
- [Differentiation Rubric](artifact/references/differentiation_rubric.md)
- [Security Review Guide](artifact/references/security_review_guide.md)
- [Publish Review Report Template](artifact/templates/publish_review_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review report with concise findings and suggested commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a publish-readiness verdict, blocking issues, risks, shortest fix path, differentiation score, and next-step command.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

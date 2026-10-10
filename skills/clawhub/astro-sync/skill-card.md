## Description:

Converts and polishes a Markdown article into an AstroPaper-compatible post for the astro_journal blog, including frontmatter and image references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Blog authors and developers use this skill to prepare an explicitly selected Markdown article for the astro_journal AstroPaper blog, copy its images, and optionally commit and publish it after approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing the wrong article or settings, or pushing content before it is ready.

Mitigation: Confirm the target article, category, draft status, featured status, and tags before writing; require separate approval before committing or pushing.

Risk: A future publication timestamp can hide a post from the blog's recent-post views.

Mitigation: Use the actual current UTC publication time rather than the date in the source filename, and check the resulting frontmatter.

Risk: An Astro build via npx may resolve packages unexpectedly.

Mitigation: Prefer a repository-local build command or skip the optional build if package-resolution risk is unacceptable.

## Reference(s):

- [astro-sync ClawHub release](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [AstroPaper Markdown post with YAML frontmatter, copied image files, and a summary of their paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the post path and copied images; commit and push require separate user approval.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Converts and polishes a selected Markdown article into an AstroPaper-compatible post for the astro_journal blog, including frontmatter and image references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Blog authors and developers use this skill to turn an explicitly selected article into an AstroPaper post, with appropriate metadata and copied images, for the astro_journal blog.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A post could be written or published with the wrong article, category, or visibility settings.

Mitigation: Confirm the article and publishing settings with the user before writing to the blog repository.

Risk: A post or copied images could be committed and pushed before the user reviews them.

Mitigation: Review the generated post and images, and require explicit approval before committing or pushing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [AstroPaper Markdown post with YAML frontmatter, copied images, and a status report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the post path and copied images; publication and git operations require separate user approval.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

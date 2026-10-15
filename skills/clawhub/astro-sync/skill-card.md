## Description:

Converts a user-selected Markdown article into an AstroPaper blog post with frontmatter and properly linked images for the astro_journal blog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Blog authors and developers use this skill to adapt approved Markdown drafts for publication in the astro_journal AstroPaper blog, including frontmatter and image references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unreviewed content or image changes could be published to the blog.

Mitigation: Confirm the selected article and publishing plan before writing; review the generated post and images, and require separate approval before commit or push.

Risk: Malformed frontmatter or missing images could break a post or leave a deployment unchanged.

Mitigation: Check frontmatter quoting and image paths, then run the build using the blog repository's locked local dependencies before publishing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance]

**Output Format:** [AstroPaper Markdown post with YAML frontmatter, copied images, and a path and image summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports postPath and imagesCopied; requires explicit approval before writing or committing and pushing.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

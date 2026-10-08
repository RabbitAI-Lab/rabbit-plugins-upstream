## Description:

Converts and lightly polishes a chosen Markdown article into an AstroPaper-compatible blog post, including frontmatter and image references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Blog authors and editors use this skill to prepare a selected Markdown article for the astro_journal AstroPaper blog, including post metadata and locally referenced images. It requires approval before writing or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect category, tags, or draft and featured settings could publish a post in the wrong form or location.

Mitigation: Confirm the chosen article and publishing settings with the user and review changed files before approving writes.

Risk: Committing or pushing before review could publish unintended changes.

Mitigation: Require separate approval for commit and push, and inspect the post and images first.

Risk: Invalid frontmatter or broken image references could prevent the post from appearing correctly.

Mitigation: Check frontmatter and image paths, then run the local locked project build where possible.

## Reference(s):

- [Astro Sync on ClawHub](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [Markdown, Image files, Text guidance]

**Output Format:** [AstroPaper Markdown post with YAML frontmatter, copied images, and a text summary of the resulting paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes only after approval; committing and pushing require separate approval.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

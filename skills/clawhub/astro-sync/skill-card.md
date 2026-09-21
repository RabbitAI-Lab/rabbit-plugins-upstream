## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io), including Astro frontmatter and image path handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to convert approved Markdown drafts into AstroPaper blog posts, copy and rewrite referenced images, and prepare the post for review before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill edits a named blog repository and may prepare content for publication.

Mitigation: Use it only for the intended AstroPaper blog workflow, require explicit user approval before writing, and require separate approval before any commit or push.

Risk: Generated posts or copied images may contain formatting, frontmatter, or content issues.

Mitigation: Review generated posts and images before publishing, and run the blog build with trusted locked dependencies where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/astro-sync)
- [Publisher profile](https://clawhub.ai/user/j3ffyang)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with generated AstroPaper-compatible post content, file paths, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a created post path and copied image list; commits and pushes only after explicit user approval.]

## Skill Version(s):

1.0.6 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

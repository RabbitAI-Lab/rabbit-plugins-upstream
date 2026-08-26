## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog, including frontmatter and image-reference updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to convert approved Markdown drafts into AstroPaper-compatible blog posts, copy images into the expected asset location, and report created post and image paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses hardcoded local blog and source-document paths that may not exist or may point to the wrong workspace.

Mitigation: Confirm the blog path and source-document locations before installing or running the skill.

Risk: Generated posts or copied images may publish incorrect content if approved without review.

Mitigation: Review generated Markdown, frontmatter, and image references before approving commits or pushes.

Risk: History or culture articles may contain claims that require additional verification.

Mitigation: Use the skill's fact-checking and corrections step before syncing those articles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown posts with YAML frontmatter, rewritten image references, file paths, and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May copy image files and propose git operations only after explicit user approval.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

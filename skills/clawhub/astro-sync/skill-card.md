## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io). Use when the user wants to publish or sync an article (e.g. from ai-thoughts/docs/ or history/docs/) to the Astro blog, convert Markdown to Astro format, add AstroPaper frontmatter, or move images into src/assets/images/.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog editors use this skill to turn a selected Markdown article into an AstroPaper-ready post for the astro_journal blog, including frontmatter and image-path handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A post or its images could be prepared for the wrong repository or published with unintended content.

Mitigation: Verify the repository path, author, Git remote, and output language; review the post and images before approving any push.

## Reference(s):

- [Astro Sync on ClawHub](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [AstroPaper-compatible Markdown post with YAML frontmatter and relative image references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a post file and may copy and rewrite image assets after explicit user approval.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

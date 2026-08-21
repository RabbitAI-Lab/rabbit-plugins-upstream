## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io).

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to convert an explicitly approved Markdown draft into an AstroPaper blog post, including frontmatter, image copying, path rewriting, and publication-ready verification steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write blog files and prepare publication changes in a local Astro repository.

Mitigation: Require explicit user approval before writing, committing, or pushing, and review the target category, tags, draft/featured state, generated post path, and copied images.

Risk: A future pubDatetime can prevent a published post from appearing in recent-post listings.

Mitigation: Use a UTC pubDatetime that has already passed and verify the generated frontmatter before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file paths, frontmatter, verification steps, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the created post path and copied image files; commits and pushes only after explicit user approval.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

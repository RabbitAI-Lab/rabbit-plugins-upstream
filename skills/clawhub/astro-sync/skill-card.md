## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog, including frontmatter and image reference updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to move an approved Markdown draft into an AstroPaper blog repository with the expected filename, frontmatter, category, tags, and copied image assets. It is intended for user-directed publishing workflows where the generated post is reviewed before commit or push.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-facing blog content can be prepared for publication.

Mitigation: Review the generated post and copied images before approving any commit or push.

Risk: The skill edits local blog files as part of a publishing workflow.

Mitigation: Require the user to identify the source article and approve the category, draft or featured status, tags, and write plan before changes are made.

## Reference(s):


## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files with YAML frontmatter plus concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May copy image files into the Astro blog asset directory and leaves commit or push actions gated on explicit approval.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

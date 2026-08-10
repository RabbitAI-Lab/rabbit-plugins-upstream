## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io).

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use astro-sync to convert an explicitly selected Markdown article into an AstroPaper-compatible blog post, including frontmatter, filename normalization, and image relocation for a local Astro journal repository.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated post or image changes may publish or update public blog content if committed and pushed.

Mitigation: Review the generated post and image changes before approving any commit or push.

Risk: An incorrect source article, category, draft status, featured status, or tag set could place content in the wrong publishing context.

Mitigation: Confirm the selected article, category, draft status, featured status, and tags before writing to the blog repository.

## Reference(s):


## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files with YAML frontmatter, copied image assets, and concise status guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user approval before writing, committing, or pushing.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Converts and polishes Markdown articles into AstroPaper-compatible blog posts for the astro_journal site, including frontmatter and image handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to sync approved Markdown drafts into an AstroPaper blog while applying required naming, frontmatter, image, and publication conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify the configured Astro blog repository by creating post files and copying images.

Mitigation: Review the proposed target path, frontmatter, body, and copied images before approving any write.

Risk: Publishing changes could be committed and pushed after files are written.

Mitigation: Require a separate explicit approval before staging, committing, or pushing changes.

Risk: Incorrect frontmatter, filenames, or image references can prevent the blog post from appearing correctly.

Mitigation: Verify category, filename, required AstroPaper frontmatter, quoted YAML values, image paths, and the optional Astro build before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/astro-sync)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown post files with AstroPaper YAML frontmatter, copied image assets, and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the created post path and copied images; requires explicit approval before writing, committing, or pushing.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

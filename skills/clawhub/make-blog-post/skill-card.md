## Description:

Helps an agent turn independently reusable code into a focused informational blog post walkthrough with destination handling, security rules, SEO shaping, and confirmation gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhauga](https://clawhub.ai/user/jhauga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to draft publishable or paste-ready blog walkthroughs for standalone reusable code. It helps choose an appropriate destination, shape the post for that venue, and keep examples free of secrets or project-specific data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may propose local post-store or workspace documentation paths before writing anything.

Mitigation: Review the first confirmation gate carefully and approve only the intended destination before files are written.

Risk: A blog draft could accidentally include sensitive or project-specific details if the source code or workspace contains them.

Mitigation: Apply the skill's security rules to replace credentials, personal data, internal URLs, account details, and prompt data with generic placeholders before delivery.

Risk: Publishing-related actions can make generated content public.

Mitigation: Use the second confirmation gate for final content review and require a separate explicit request for committing, pushing, uploading, or posting.

## Reference(s):

- [Common Blog Platforms](references/blog-platforms.md)
- [Pseudo-Blog Venues](references/pseudo-blog-venues.md)
- [SEO Optimization](references/seo-optimization.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Guidance, Configuration instructions]

**Output Format:** [Markdown post content, optional post files, and concise hand-off guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include front matter, title, description, slug, tags, destination path, and venue-specific posting notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

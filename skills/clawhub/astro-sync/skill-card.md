## Description:

Convert and polish a Markdown article into AstroPaper-compatible post format for the astro_journal blog (everbox.io).

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and blog maintainers use this skill to convert approved Markdown drafts into AstroPaper blog posts, add required frontmatter, copy referenced images, and prepare publication changes after explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can write blog post files and image assets to a specific Astro blog checkout.

Mitigation: Confirm that the configured astro_journal and source article paths are the intended repositories before allowing writes.

Risk: The skill can commit and push publication changes after approval.

Mitigation: Review the generated post, copied images, and staged changes before approving commit or push.

## Reference(s):


## Skill Output:

**Output Type(s):** [markdown, files, shell commands, guidance]

**Output Format:** [Markdown files, copied image files, and concise status messages with approval prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the created post path and copied or missing images; commit and push commands are approval-gated.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

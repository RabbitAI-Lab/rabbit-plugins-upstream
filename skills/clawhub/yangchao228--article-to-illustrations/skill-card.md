## Description:

Plan, generate, insert, and hand off evidence-safe illustrations for reviewed long-form Markdown articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangchao228](https://clawhub.ai/user/yangchao228)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and content production agents use this skill to decide whether reviewed long-form Markdown articles need illustrations, then plan image slots, generate or accept local assets, insert relative Markdown image references, and prepare an image manifest for publishing handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Illustration plans or generated images could imply unsupported evidence, invented UI, metrics, quotations, logos, or outcomes.

Mitigation: Review each image plan and generated asset against the source article before insertion, and label conceptual visuals as illustrations.

Risk: Publishing workflows could upload images or rewrite Markdown URLs before the user has confirmed the plan.

Mitigation: Use the documented approval gates and run md-img-r2 in plan mode before upload or Markdown rewrite.

Risk: Paid image tools, screenshots, or public publishing steps may introduce cost, rights, or disclosure concerns.

Mitigation: Require explicit user confirmation before multi-image generation, paid service use, screenshot editing, upload, or external publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yangchao228/skills/article-to-illustrations)
- [OpenClaw Homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/article-to-illustrations)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown tables and bullet lists with image plans, insertion notes, manifest entries, and handoff status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local relative image paths, alt text, dimensions, checksums, R2 state, and confirmation gates for upload or publishing handoff.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

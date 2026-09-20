## Description:

Plan, generate, insert, and hand off evidence-safe illustrations for reviewed long-form Markdown articles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and publishing agents use this skill to decide when long-form articles need illustrations, plan evidence-bound image slots, insert reviewed local images into Markdown, and prepare a manifest for upload handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create local image files and edit reviewed Markdown after approval.

Mitigation: Confirm the image plan and generation scope first, then review inserted Markdown paths and the image manifest before accepting changes.

Risk: Generated or edited visuals could misstate source evidence, labels, product interfaces, metrics, quotes, logos, or outcomes.

Mitigation: Tie every slot to source anchors and factual constraints, label conceptual visuals as illustrations, and check each image before insertion.

Risk: Uploads, public URL rewrites, or publishing could expose files before final review.

Mitigation: Use md-img-r2 in plan mode first and require explicit confirmation before upload, Markdown rewrite, or external publishing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentforge-cyber/skills/article-to-illustrations)
- [Project Homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/content/article-to-illustrations)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown plan with image slots, inserted-file summary, image manifest, and handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit approval before generating multiple images, uploading files, rewriting Markdown with public URLs, or publishing externally.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

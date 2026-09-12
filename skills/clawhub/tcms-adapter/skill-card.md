## Description:

Channel-adaptation agent that adapts reviewed core drafts or published articles into channel-specific publish-ready marketing versions and re-promotion material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and communications teams use this skill to turn approved core drafts or published articles into channel-specific drafts for WeChat, developer communities, Chinese social posts, English X posts, LinkedIn summaries, and sales one-pagers. It is intended for adaptation and re-promotion, not original drafting or direct publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Adapted drafts could change or invent data points from the reviewed source.

Mitigation: Review outputs against the source draft or article and preserve only supported data points before publishing.

Risk: Customer names or sensitive details could appear in generated channel drafts.

Mitigation: Carry forward source redactions, auto-redact unredacted customer names where detected, and run human review before publication.

Risk: English channel drafts may include uncertain wording or require localization review.

Mitigation: Treat copy marked for confirmation as requiring human proofreading before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown files and execution summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces channel-specific adapted drafts under content/adapted/ and flags channels or English copy that need confirmation.]

## Skill Version(s):

1.1.5 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

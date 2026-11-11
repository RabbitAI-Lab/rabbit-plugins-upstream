## Description:

This skill should be used when a fact-checked and compliance-approved final Markdown draft needs to be turned into multi-channel publishing assets — WeChat article (135-editor-compatible inline HTML), WeChat image-summary card (公众号发图/摘要图/图文卡/810×1080), LinkedIn post, standalone responsive HTML page, and an archive ledger (local record plus optional Notion entry). It only orchestrates publishing and format conversion; it does not repeat fact-checking and does not auto-publish.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams and writers use the skill to turn a fact-checked, compliance-approved Markdown draft into channel-ready publishing assets for WeChat, LinkedIn, a responsive web page, and an archive. It prepares materials for review and manual publishing; it does not auto-publish.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated security review had incomplete component coverage: 11 of 12 components were fully inspected.

Mitigation: Review the scripts and remaining component coverage before installation if those details matter.

Risk: Using an unreviewed draft could carry unchecked claims into channel-ready publishing materials.

Mitigation: Use the skill only after the draft has passed fact-checking and compliance review.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/content-publishing-suite-skill)
- [WeChat style guide](artifact/references/wechat-style.md)
- [Channel contracts](artifact/references/channel-contracts.md)
- [WeChat layout baseline](artifact/references/wechat_layout_baseline.json)

## Skill Output:

**Output Type(s):** [HTML, Markdown, JSON, Image assets]

**Output Format:** [A publishing package with inline WeChat HTML, Markdown copy, responsive HTML, JSON archive records, and a summary-card image.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an already reviewed final draft; assets are prepared for human review and are not published automatically.]

## Skill Version(s):

1.1.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Channel-adaptation agent that adapts a reviewed core draft into channel-specific publish-ready versions and re-promotion material for existing content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and content teams use this skill to adapt already-reviewed technical product drafts into WeChat, developer-community, Chinese social, English X, LinkedIn, and sales one-pager formats. It is intended for channel adaptation and re-promotion, not original drafting or direct publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch a provided article URL and create adapted marketing drafts from that content.

Mitigation: Use it only with content intended for repurposing and review generated drafts before publication.

Risk: Channel adaptations can introduce misleading wording, dropped context, or inconsistent product naming if outputs are published without review.

Mitigation: Check source-data preservation, brand naming, customer redaction, and English wording before approving any channel version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/tcms-adapter)
- [Developer community channel specification](references/channel-specs/dev-community.md)
- [LinkedIn channel specification](references/channel-specs/linkedin.md)
- [WeChat official account channel specification](references/channel-specs/wechat-official.md)
- [X overseas channel specification](references/channel-specs/x-overseas.md)
- [Sales one-pager template](references/templates/one-pager.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files, Guidance]

**Output Format:** [Markdown files and concise execution summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes adapted channel drafts under content/adapted/ when executed in a workspace.]

## Skill Version(s):

1.1.6 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

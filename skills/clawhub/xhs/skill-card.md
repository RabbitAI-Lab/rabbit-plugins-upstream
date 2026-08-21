## Description:

Helps creators draft, save, publish, manage, and review Xiaohongshu posts through the official Creator Center with browser automation and explicit user confirmation before public publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, operators, agencies, and teams use this skill to prepare Xiaohongshu content, format topic chips, save drafts, publish with confirmation, reply to messages, and inspect visible Creator Center metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Draft-saving guidance may target the red publish control, creating a risk of unintended public posting.

Mitigation: Review and correct the draft workflow before use, verify the draft/save control separately from the publish control, and require explicit confirmation immediately before any public post.

Risk: The skill operates against a real Xiaohongshu account through browser automation.

Mitigation: Use only with an authorized logged-in account, do not bypass captchas, SMS verification, or platform risk controls, and keep account replies or publishing actions gated by user confirmation.

## Reference(s):

- [Post Templates](references/post-templates.md)
- [Xiaohongshu Creator Center](https://creator.xiaohongshu.com)
- [Xiaohongshu Creator Center Publish Page](https://creator.xiaohongshu.com/publish/publish?from=menu&target=image)
- [ClawHub Skill Page](https://clawhub.ai/mebusw/skills/xhs)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown status summary with drafted post content, selected mode, result status, topic-chip details, and next steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require browser interaction with a logged-in Creator Center session; public publishing and account replies require explicit user confirmation.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

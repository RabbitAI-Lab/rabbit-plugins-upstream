## Description:

将当前会话中的真实对话整理为可发布的 Markdown 文章、竖版分享卡片或两者兼有，并在缺少可读取历史记录时停止。

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

Apache 2.0

## Use Case:

面向希望复用或分享 AI 协作过程的用户，将当前会话整理成有据可查的文章和分享卡片。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may export another project's private conversation without asking you to select it.

Mitigation: Select and verify the intended --session-file for both checking and export, choose the output mode, review generated files before sharing, and keep transcripts and temporary HTML private.

## Reference(s):

- [Source repository](https://github.com/weikion/chat-to-content)
- [ClawHub skill page](https://clawhub.ai/weikion/skills/chat-to-content)
- [Session extraction guide](references/extraction.md)
- [Article writing guide](references/article.md)
- [Share card guide](references/cards.md)

## Skill Output:

**Output Type(s):** [Markdown, Images, JSON]

**Output Format:** [Markdown article, PNG or JPG share cards, and reproducible JSON card data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires readable conversation history; article, cards, or both can be selected.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

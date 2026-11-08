## Description:

Turns a substantive user–agent conversation into a publishable summary article or vertical share cards, using details grounded in the conversation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

MIT-0

## Use Case:

People who want to turn a substantive conversation with an agent into shareable content use this skill to create an article or social cards and prepare the files for publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic cross-workspace fallback can select an unrelated private conversation and turn it into shareable content.

Mitigation: Remove the fallback or require an explicitly verified --session-file for both checking and extraction, and confirm the conversation identity before use.

Risk: A transcript or generated article and cards may contain sensitive details; temporary rendering files may retain conversation content.

Mitigation: Keep the raw transcript private, review every output for sensitive details before sharing, and clean up temporary rendering files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/weikion/skills/chat-to-content)
- [Publisher profile](https://clawhub.ai/user/weikion)
- [Article writing guidance](artifact/references/article.md)
- [Share card guidance](artifact/references/cards.md)
- [Content extraction guidance](artifact/references/extraction.md)

## Skill Output:

**Output Type(s):** [Markdown article, PNG/JPG share cards]

**Output Format:** [Markdown and PNG/JPG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses conversation-grounded content; article, cards, or both may be produced depending on the requested output.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

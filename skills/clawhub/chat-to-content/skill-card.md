## Description:

Turns the current conversation into a Markdown article or vertical share cards (PNG/JPG), using only the session identified by the runtime.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weikion](https://clawhub.ai/user/weikion)

### License/Terms of Use:

MIT-0

## Use Case:

People who have had a substantive conversation can use the skill to turn the current chat into a publishable Markdown article, vertical share cards, or both. It is intended for the current session and does not summarize external documents or other conversations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some conversation titles or previews may not receive the documented redaction before content is published.

Mitigation: Use conversations suitable for sharing and inspect generated content before publishing; request title and preview redaction before relying on the privacy claims.

Risk: The Playwright fallback may run without the environment filtering described in the security guidance.

Mitigation: Run without secret-bearing environment variables until environment filtering is corrected.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/weikion/skills/chat-to-content)

## Skill Output:

**Output Type(s):** [Markdown, PNG images, JPG images]

**Output Format:** [Markdown article and vertical share-card image files]

**Output Parameters:** [Variable number of files, depending on the selected output mode]

**Other Properties Related to Output:** [The user can request an article, cards, or both; card images support PNG and JPG formats.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

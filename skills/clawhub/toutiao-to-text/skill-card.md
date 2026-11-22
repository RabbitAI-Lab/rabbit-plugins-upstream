## Description:

Extracts text from Toutiao articles and videos, including article content, image descriptions and text, timed video transcripts, and sourced key points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users share Toutiao article or video links when they need readable article text, image descriptions and text, timed transcripts, or sourced key points for summarizing or rewriting. An agent runs the command-line client and presents the returned content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing a Toutiao link sends it to the external LinkDigest service.

Mitigation: Share only links you are comfortable processing through that service, and review the reported coverage before relying on the result.

Risk: Full requests can use service credits, and an optional LINKDIGEST_API_KEY is read from the runtime environment.

Mitigation: Keep the key in an environment variable, never paste it into chat, and use --max-credits to set a per-request spending limit.

## Reference(s):

- [LinkDigest Toutiao API guide](https://linkdigest.dev/zh/toutiao-api?ref=skill-toutiao-to-text)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/toutiao-to-text)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON containing extracted article text, image text, video transcripts, and key points]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include translation; reports coverage and degraded results when content is unavailable. Requests may consume service credits.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter; release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

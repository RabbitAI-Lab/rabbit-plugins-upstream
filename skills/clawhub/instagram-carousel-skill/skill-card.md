## Description:

Plans and writes Instagram carousels, renders 1080×1350 JPEG slides with alt text and captions, and can publish through WoopSocial after user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT

## Use Case:

Creators, developers, and small businesses use this skill to turn a topic, product, or brand idea into a designed Instagram carousel with a caption and alt text, then optionally publish it after reviewing and approving the post.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key placed in a URL may be saved or logged.

Mitigation: Prefer OAuth, avoid the API-key-in-URL fallback, protect credential-bearing configuration, redact URLs from diagnostics, and rotate any key that has been exposed.

Risk: Slides are uploaded to WoopSocial before final publishing approval.

Mitigation: Upload only media you intend to share with WoopSocial, and review the slides, caption, and destination account before approving publication.

## Reference(s):

- [Carousel Formats](references/carousel-formats.md)
- [Design Rules](references/design-rules.md)
- [Instagram Platform Facts](references/instagram-2026.md)
- [WoopSocial Setup and Posting Guide](references/woopsocial.md)
- [WoopSocial MCP Tools Reference](https://docs.woopsocial.com/mcp/tools-reference)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, JPEG images]

**Output Format:** [Carousel slide copy, caption and alt text; carousel specification JSON; rendered JPEG slides]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slide images are rendered at 1080×1350 pixels; publishing requires user approval.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

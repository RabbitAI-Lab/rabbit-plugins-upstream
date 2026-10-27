## Description:

Searches indexed public Xiaohongshu notes by topic and turns selected links into text with image OCR, transcripts, visible comments, and engagement counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can find public Xiaohongshu posts for product research, competitor review, creator discovery, and customer feedback, then read selected posts as structured text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Topics and submitted links or share text are sent to LinkDigest, which states that it retains text results; search and reading also consume credits.

Mitigation: Use a spending-limited API key, select notes before reading, and set --max-credits to cap per-note reading costs.

## Reference(s):

- [LinkDigest Xiaohongshu research](https://linkdigest.dev/zh/xiaohongshu-shichang-diaoyan?ref=skill-xiaohongshu-search-to-text)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [LinkDigest browser extension](https://linkdigest.dev/extension)
- [LinkDigest MCP](https://linkdigest.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON search results and selected note digests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post text, image OCR, video transcripts, visible comments, key points, and engagement counts.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

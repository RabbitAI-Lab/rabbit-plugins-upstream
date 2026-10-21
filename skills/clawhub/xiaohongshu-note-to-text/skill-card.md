## Description:

Converts individual Xiaohongshu notes into readable text, including image OCR, captions, metadata, and optional consumer insights or video transcripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People analyzing or documenting Xiaohongshu notes use this skill to extract captions and text from images, review engagement and share-page comments, and optionally request consumer insights or video transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted note links or share text can contain access-token parameters and are sent to LinkDigest.

Mitigation: Submit only public, non-sensitive links and review share text before sending it.

Risk: Text results are cached by link and may be returned to other users requesting the same public link.

Mitigation: Do not submit private or sensitive content; review the service privacy policy before use.

Risk: The optional unpinned npx MCP bridge adds a third-party dependency.

Mitigation: Prefer the included Python script, or pin and independently trust the MCP bridge dependency.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/xiaohongshu-note-to-text)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Analysis]

**Output Format:** [Markdown by default; optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-image OCR, note metadata and available share-page comments; optional consumer insights and video transcripts. Without an API key, only a limited free summary is available.]

## Skill Version(s):

1.1.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

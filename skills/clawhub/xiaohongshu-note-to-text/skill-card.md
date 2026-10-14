## Description:

Extracts text, image OCR, descriptions, and note details from public Xiaohongshu links or share text using LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to turn public Xiaohongshu image or video notes into readable text for review, research, summarization, or translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links, share text, URL parameters, and the LinkDigest API key are sent to an external service.

Mitigation: Submit only public, non-sensitive notes and use a dedicated API key stored outside prompts and shared files.

Risk: The optional MCP setup runs an unpinned npx package.

Mitigation: Prefer the included Python client, or pin and independently trust the MCP package before using it.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/xiaohongshu-note-to-text)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include captions, image OCR, descriptions, tags, interaction counts, and video transcripts; without an API key, the free result is a summary.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

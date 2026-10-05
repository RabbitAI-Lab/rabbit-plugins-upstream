## Description:

Extracts public Xiaohongshu note text, image OCR, image descriptions, key points, tags, and engagement snapshots through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and researchers use this skill to turn a user-supplied public Xiaohongshu note link or share text into readable content, including text found in images and available engagement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links and the LinkDigest API key are sent to a paid external service; results may be cached by link.

Mitigation: Submit only public links you are comfortable sharing, avoid private or login-only content, and keep the API key out of chats and source control.

Risk: Processing a note may incur credits, especially with optional analysis or translation.

Mitigation: Use --max-credits to cap spending before submitting a note.

Risk: The optional npx MCP bridge uses an unpinned package path.

Mitigation: Prefer the bundled Python client or direct HTTPS API unless the bridge package has been separately reviewed.

Risk: OCR can misread stylized or small text, and engagement figures may be cached snapshots.

Mitigation: Check important names and numbers against the original images and label engagement figures as snapshots.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/linkdigest-xhs-note-ocr)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data]

**Output Format:** [Markdown by default; JSON optionally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ordered image OCR, descriptions, key points, tags, engagement snapshots, and credits used.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

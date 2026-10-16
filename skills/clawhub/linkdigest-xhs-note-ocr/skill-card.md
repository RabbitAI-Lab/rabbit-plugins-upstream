## Description:

Extracts Xiaohongshu note captions, image text, image descriptions, key points, and engagement statistics from shared links using LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People researching or archiving public Xiaohongshu notes use this skill to turn shared links into readable captions and per-image OCR, with optional summaries and engagement snapshots. Full image text requires a LinkDigest API key; a limited summary is available without one.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links or share text are sent to LinkDigest and third-party model processors; cached text from public links may be reused.

Mitigation: Submit only public, nonsensitive links and review LinkDigest's privacy policy before use.

Risk: Exposing the API key in chats or commits can allow unauthorized use.

Mitigation: Keep the key in an environment variable or private configuration; never paste it into chats or commit it.

Risk: The optional unpinned npx MCP command can fetch a dependency whose contents change.

Mitigation: Prefer the bundled Python or curl workflow, or pin and review the MCP dependency before running it.

Risk: OCR can misread stylized or small text, including prices, numbers, and brand names.

Mitigation: Check consequential details against the original images and distinguish extracted note text from model-generated descriptions.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; optional JSON with captions, per-image OCR, descriptions, key points, tags, and engagement statistics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Engagement figures are snapshots; image descriptions and key points are model-generated, and OCR may misread small or stylized text. Reports credits used or cache hits.]

## Skill Version(s):

1.2.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

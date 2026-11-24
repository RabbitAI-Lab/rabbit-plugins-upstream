## Description:

Extracts text, per-image OCR, image descriptions, key points, and engagement data from a single Xiaohongshu note through LinkDigest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a Xiaohongshu note link or share text to retrieve its caption, text recognized from each image, image descriptions, key points, tags, and engagement counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports capabilities broader than the declared Xiaohongshu OCR purpose, and the scan was incomplete.

Mitigation: Review the complete skill and confirm the platforms and processing options before use.

Risk: Submitted content is sent to LinkDigest, and paid processing can consume API credits.

Mitigation: Avoid private or sensitive links, review LinkDigest's privacy information, and set a spending limit on the API key.

Risk: The optional mcp-remote bridge is unpinned and carries supply-chain exposure.

Mitigation: Skip the bridge unless needed; if used, pin and review the package version before installation.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-linkdigest-xhs-note-ocr)
- [LinkDigest privacy information](https://linkdigest.dev/privacy)
- [LinkDigest OpenAPI specification](https://linkdigest.dev/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON containing note text, per-image OCR and descriptions, key points, tags, and engagement metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on source availability; full output requires a LinkDigest API key and may consume credits.]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

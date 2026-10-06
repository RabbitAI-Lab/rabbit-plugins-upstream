## Description:

从小红书笔记链接或分享文案提取正文、逐图 OCR 文字、图片描述、要点和互动信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, researchers, and content creators use this skill to turn an accessible Xiaohongshu note into searchable text, including words embedded in images, without signing in to Xiaohongshu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links or share text and an API key are sent to LinkDigest; text results are cached by link and may be reused for the same public link.

Mitigation: Submit only public, non-sensitive links and keep the API key out of chats and shared files.

Risk: Usage consumes paid credits, and the optional unpinned npx MCP route runs an external package.

Mitigation: Set a per-request credit limit when cost matters and avoid the optional npx route unless its package source is trusted.

Risk: OCR can misread small or stylized text, and cached interaction counts may be stale.

Mitigation: Check important names and numbers against the original images and treat counts as dated snapshots.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)
- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-xhs-note-ocr)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; structured JSON on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes note text, per-image OCR, model-generated descriptions and key points, available interaction counts, and credit/cache status.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

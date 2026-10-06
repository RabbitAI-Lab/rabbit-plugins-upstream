## Description:

Extracts the full text and image OCR from a public WeChat article into Markdown, with article details, key points, links, and reading coverage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read a supplied public WeChat article, including text embedded in images, for summarization, research, or knowledge-base capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article links and the API key are sent to LinkDigest for processing.

Mitigation: Use only public WeChat article links; do not submit private or internal links, and keep the API key in environment or skill configuration rather than chat.

Risk: Paid processing may consume credits, and image OCR may miss or misread text.

Mitigation: Use the documented WeChat workflow and a per-request credit limit; inspect coverage and verify important names, numbers, and prices against the original images.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jackchew7143/skills/linkdigest-wechat-article-reader)
- [LinkDigest documentation](https://linkdigest.dev/zh/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown by default; optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes article text, per-image OCR, key points, links, coverage, and credit usage; unread portions are identified.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

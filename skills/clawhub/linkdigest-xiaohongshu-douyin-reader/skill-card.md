## Description:

Reads public Xiaohongshu and Douyin posts through LinkDigest to provide captions, image text, video transcripts, summaries, and optional English translations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Xiaohongshu or Douyin posts use this skill to read and translate one public post at a time without a platform account, including captions, text in images, and spoken video content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links or copied share text are sent to LinkDigest, and results may be cached by link.

Mitigation: Submit only public, nonsensitive posts and avoid private links or sensitive share text.

Risk: Extracting or translating a post may consume paid credits.

Mitigation: Set --max-credits before submitting a link to cap spending.

Risk: OCR, translations, summaries, and model-written key points may be inaccurate or incomplete.

Mitigation: Check important claims against the original post and disclose uncaptured content.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/docs)
- [LinkDigest API key setup](https://linkdigest.dev/app/keys)
- [LinkDigest pricing](https://linkdigest.dev/pricing)
- [ClawHub skill listing](https://clawhub.ai/jackchew7143/skills/linkdigest-xiaohongshu-douyin-reader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown by default; JSON on request]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include captions, image OCR, timestamped transcripts, translations, key points, coverage gaps, and credit usage.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

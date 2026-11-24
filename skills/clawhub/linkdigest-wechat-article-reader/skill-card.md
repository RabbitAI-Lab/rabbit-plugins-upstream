## Description:

微信公众号文章提取：把 mp.weixin.qq.com 文章链接读成全文 Markdown，连文章里每张图片上的文字一起 OCR。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jackchew7143](https://clawhub.ai/user/jackchew7143)

### License/Terms of Use:

MIT-0

## Use Case:

External users can provide a public WeChat article link to receive its article text, image OCR, key points, author and date, and links found in the article. Use it for reading or summarizing one article at a time; a LinkDigest API key is needed for the full output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted links are processed by LinkDigest, and results for public links may be cached and shared with other users.

Mitigation: Submit only links you are comfortable sharing with LinkDigest; do not submit internal or private links.

Risk: Full processing and optional analysis or translation can consume paid credits.

Mitigation: Review the current pricing and use the maximum-credit option when you need to cap spend.

## Reference(s):

- [LinkDigest documentation](https://linkdigest.dev/zh/docs?ref=skill-linkdigest-wechat-article-reader)
- [LinkDigest privacy policy](https://linkdigest.dev/privacy)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON containing article text, OCR text, summaries, and extracted links]

**Output Parameters:** [1D (one article link per invocation)]

**Other Properties Related to Output:** [Image OCR is limited to 60 images; available content can depend on the account's credit budget.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

AIGC text generation uses large language models to generate text from prompts and can analyze combined text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate copy, translations, summaries, data-analysis narratives, and image or video content analysis through LinkFox's hosted text-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media URLs are sent to LinkFox's remote service.

Mitigation: Avoid sending secrets, regulated data, or media URLs that should not be processed by the hosted service.

Risk: The skill can assist with account login, API key issuance, and payment-order workflows.

Mitigation: Treat SMS codes, API keys, payment links, and QR codes as sensitive credential or billing material.

Risk: LINKFOX_* endpoint environment variables can change where requests are sent.

Mitigation: Verify endpoint environment variables point to trusted LinkFox hosts before use.

## Reference(s):

- [AI 生文 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-textgen)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Plain text content or JSON task response/envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May flatten newlines in generated content, save large responses to a local file, and return a savedPath envelope.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

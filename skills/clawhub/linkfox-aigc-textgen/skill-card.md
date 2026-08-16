## Description:

Generates text from prompts and can combine text with image or video URLs for content analysis, writing, translation, and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate product copy, titles, translations, analytical summaries, and media-aware text from prompts plus optional image or video URLs. It can also guide users through LinkFox authentication and billing recovery when API access or balance issues block generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide users through SMS login, API-key issuance, plan listing, payment order creation, and payment QR display.

Mitigation: Install only in environments where LinkFox endpoint configuration is trusted, review account and billing steps before use, and treat any displayed API key as a secret.

Risk: Prompts and media URLs are sent to remote LinkFox text-generation endpoints for processing.

Mitigation: Avoid submitting sensitive prompts, image URLs, or video URLs unless remote processing by the service is acceptable.

Risk: Generated text can be consumed by downstream image or video generation skills.

Mitigation: Review generated prompts before chaining them into downstream creation workflows, especially for commercial or brand-sensitive outputs.

## Reference(s):

- [AI 生文 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text or JSON, with Markdown guidance and shell commands for setup and recovery workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated content may be newline-flattened with a visible placeholder for downstream chaining; large responses may be saved to a local JSON file and summarized in stdout.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes publicly accessible image URLs with LinkFox multimodal AI to describe visual content, extract visible text, and answer image-specific questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze images from URLs, extract text from screenshots or product images, and get concise visual descriptions or answers through the LinkFox image recognition API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs and uploaded local images are sent to LinkFox for processing, and uploaded files become publicly accessible by URL for a limited period.

Mitigation: Use only images that are acceptable to disclose to LinkFox and avoid confidential screenshots, documents, personal photos, regulated data, credentials, or unreleased business materials.

Risk: The skill supports paid-credit workflows and can guide users through plan selection and payment.

Mitigation: Confirm the provider, plan, price, and payment method before starting any billing flow, and avoid repeated API calls without user approval because image analysis consumes credits.

Risk: The skill relies on LinkFox API keys and account onboarding, including phone verification flows.

Mitigation: Store API keys in the documented environment variables, keep verification codes and tokens out of shared logs, and rotate credentials if they may have been exposed.

Risk: Full API responses are written to local session data and may include image analysis content or usage metadata.

Mitigation: Review and remove saved response files when they contain sensitive content or when local retention is not desired.

## Reference(s):

- [图片识别 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-multimodal-recognize-image)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON API responses and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large API responses are summarized by default, while full responses are saved to local session data.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

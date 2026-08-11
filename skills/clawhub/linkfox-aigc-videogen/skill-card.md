## Description:

Generates short AI videos from a source image and optional ending frame using LinkFox-backed models such as KLING, WAN, SEED, SEED_FAST, and HAILUO.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a provided image, prompt, and model settings into a generated video file. It is suited for single-image or first-frame/last-frame video generation workflows, including product and scene videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The onboarding flow can request a phone number and SMS code and return an API key.

Mitigation: Use the onboarding flow only when you intend to register or log in with LinkFox, and do not share SMS codes or generated API keys outside the intended LinkFox setup.

Risk: Billing recovery can list plans and create payment orders or QR payment flows.

Mitigation: Confirm the selected plan, price, and payment method before creating an order or authorizing payment.

Risk: Configurable service base-url environment variables can change where requests are sent.

Mitigation: Keep LinkFox service environment variables pointed at official LinkFox domains unless an administrator has approved another endpoint.

Risk: Images, prompts, and generated media are processed through a third-party LinkFox service.

Mitigation: Avoid submitting sensitive or unauthorized images and prompts, and confirm that the use case permits third-party processing.

## Reference(s):

- [AI 生视频 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Configuration guidance]

**Output Format:** [Plain text with local video file paths, JSON parameter examples, and shell commands for onboarding when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates an asynchronous video-generation task, polls for completion, and saves generated video media to the session media directory.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

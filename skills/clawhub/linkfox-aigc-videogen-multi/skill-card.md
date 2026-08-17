## Description:

AIGC多场景视频生成 uses LinkFox asynchronous video-generation APIs to create videos from multiple reference images and a prompt, with support for KLING, SEED, SEED_FAST, and HAPPY_HORSE model options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit reference image URLs and generation parameters to LinkFox services, then receive local paths to generated video files after asynchronous task polling completes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends image URLs, prompts, and generated outputs to LinkFox services and stores generated media or responses locally.

Mitigation: Use only approved inputs, avoid sensitive media unless authorized, and apply local retention and access controls to generated files.

Risk: The support flow can handle phone/SMS login, API-key generation, account lookup, and payment ordering.

Mitigation: Prefer obtaining an API key directly from the official LinkFox site, and review any plan, order, payment URL, or QR code before paying.

Risk: Endpoint variables can redirect traffic if misconfigured.

Mitigation: Verify LINKFOX_* endpoint variables point to expected LinkFox HTTPS hosts before using the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aigc-videogen-multi)
- [Multi-image video API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, shell commands, and local file paths for generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates asynchronous LinkFox API tasks, polls until success or failure, stores generated videos in a local session media directory, and stores raw responses locally when no video file is available.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Flyelep Generate Kits is a bundle of agent skills for using Flyelep API workflows that generate ecommerce posters, edit images, write creative copy, and generate product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill bundle to guide agents through authenticated Flyelep API calls for ecommerce poster creation, image matting, translation, enlargement, clarity enhancement, scene and product replacement, prompt writing, hot-image and hot-video replication, and text-to-video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Flyelep API calls require a secretKey credential.

Mitigation: Collect the key at runtime, avoid storing it in skill files or persistent configuration, and avoid echoing it into logs or shared transcripts.

Risk: Requests may send prompts, product media, image URLs, video URLs, or audio URLs to Flyelep services.

Mitigation: Do not submit confidential prompts, private media, internal URLs, or sensitive customer assets unless the user has confirmed they are appropriate to process through the service.

Risk: Some Windows workflows create temporary JSON payload files that may contain request data or credentials.

Mitigation: Use runtime secret handling where possible and delete temporary payload files immediately after each API call.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-generate-kits)
- [Flyelep platform](https://www.flyelep.cn)
- [Flyelep control board](https://www.flyelep.cn/controlboard)
- [Root skill index](artifact/SKILL.md)
- [Generate poster skill](artifact/skills/generate-poster/SKILL.md)
- [Generate video skill](artifact/skills/generate-video/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples, JSON payloads, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include API call instructions and returned media URLs; some workflows require polling asynchronous task results.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

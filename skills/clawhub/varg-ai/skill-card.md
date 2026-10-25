## Description:

Generate AI videos, images, speech, and music with Varg for rendered media, slideshows, talking characters, product showcases, social content, or single-asset generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securityqq](https://clawhub.ai/user/securityqq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate AI images, video, speech, music, and rendered media through Varg's cloud API or local rendering workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance can automatically update skills beyond this release.

Mitigation: Review changes and perform updates manually, limited to this skill.

Risk: The setup flow can persist or expose the Varg API key.

Mitigation: Keep credential storage optional, restrict access to stored credentials, and use a silent key check.

Risk: Generation inputs may be sent to Varg or its providers for processing.

Mitigation: Avoid sending media that is not approved for external processing.

Risk: Generation and rendering can incur usage costs.

Mitigation: Use a dedicated project directory and agree on a spending limit before running jobs.

## Reference(s):

- [Varg AI](https://varg.ai)
- [ClawHub release](https://clawhub.ai/securityqq/skills/varg-ai)
- [Gateway API guide](references/gateway-api.md)
- [Cloud rendering guide](references/cloud-render.md)
- [Local rendering guide](references/local-render.md)
- [Prompting guide](references/prompting.md)

## Skill Output:

**Output Type(s):** [Files, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance, shell commands and code; generated image, video, speech, and music files or links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media and rendering instructions depend on the requested task and selected workflow.]

## Skill Version(s):

2.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

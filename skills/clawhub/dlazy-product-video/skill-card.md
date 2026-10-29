## Description:

product video, product demo video, product ad video, product showcase — turn a product's photos or link into a polished demo / ad video. Use when the user wants a product demo, showcase, or ad video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and marketing teams use this skill to turn product photos, specifications, manuals, catalogs, or storefront links into short product showcase and advertising videos, with optional multilingual voiceover and a virtual host.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to dLazy's hosted service, and attached files are uploaded to its media storage.

Mitigation: Send only material approved for that service and review its data-retention terms.

Risk: The workflow uses an organization API key, saved project context, and paid credits.

Mitigation: Protect the API key, select the intended project, and review credit costs before generating videos.

Risk: The bundled review covers the skill instructions, not a full audit of the external CLI or hosted service.

Mitigation: Review the CLI package and service terms before sending sensitive prompts or product files.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [Generated product video files with streamed text responses from the hosted agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video content depends on the selected product template and supplied materials; multilingual voiceover and a virtual host are optional.]

## Skill Version(s):

1.0.32 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

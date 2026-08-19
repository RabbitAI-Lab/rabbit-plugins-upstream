## Description:

Creates and edits AliExpress product listing images, variant galleries, compatibility graphics, package-content images, and multi-country localization bases using reference-guided AI Hive image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce operators, and developers use this skill to generate AliExpress listing image bases, SKU variant galleries, connector and compatibility graphics, package-content images, and localized market visuals for later human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product and reference images are uploaded to AI Hive for generation.

Mitigation: Use only media that is approved for AI Hive processing and avoid uploading sensitive or restricted product imagery.

Risk: The skill stores or reads an AI Hive API key locally.

Mitigation: Use the documented initialization flow or environment variable, keep the local config file private, and rotate the key if it is exposed.

Risk: The bundled script includes generic AI Hive client functions beyond the documented image generation flow.

Mitigation: Use the documented generate, task, upload, and init commands unless broader AI Hive account or media operations are intentionally required.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/aliexpress-ecommerce-image-generation-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files, JSON]

**Output Format:** [Markdown guidance with bash command examples, local configuration, downloaded image files, and optional JSON task output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses reference images, batch size, routing mode, output directory, and no-download/task lookup options; generated media is downloaded locally when task polling succeeds.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

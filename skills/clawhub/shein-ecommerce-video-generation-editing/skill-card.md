## Description:

Create and edit SHEIN fashion try-on videos, garment movement clips, fabric details, colorway variants and outfit styling content for ecommerce production using AI Hive Seedance video generation and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce marketers, SHEIN marketplace sellers, and content production teams use this skill to generate and edit fashion try-on, garment detail, colorway, outfit, and model-material videos. It helps agents prepare AI Hive CLI commands while preserving garment construction, model continuity, approved SKU attributes, and platform review constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key, and init saves the key locally under ~/.ai-hive/config.json.

Mitigation: Use a scoped key where possible, keep the local config file permissions restricted, prefer environment or CLI injection in shared environments, and rotate the key if it is exposed.

Risk: Selected media may be uploaded to AI Hive and object storage during generation.

Mitigation: Use only intended, approved media files; avoid uploading sensitive or unlicensed assets; and confirm consent and usage rights before processing model or product imagery.

Risk: Generated ecommerce videos can misrepresent garment fit, body shape, material behavior, SKU attributes, or advertising claims.

Mitigation: Review outputs against approved reference material, preserve model and garment attributes, avoid unsupported performance or trend claims, and check current SHEIN product and advertising rules before publication.

Risk: The configured AI Hive base URL controls where API requests and uploads are sent.

Mitigation: Review the configured base URL before execution and use the default service endpoint only when it matches the intended deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/shein-ecommerce-video-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash command examples and CLI-produced JSON or downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; generated media is downloaded to the configured output directory unless no-download is used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

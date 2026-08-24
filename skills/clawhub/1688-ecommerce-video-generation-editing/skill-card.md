## Description:

Generates and edits 1688 ecommerce videos for product demos, factory workflows, OEM/ODM customization, quality inspection, packaging, logistics, and B2B inquiries using Seedance and AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, suppliers, and their agents use this skill to prepare 1688-focused product, factory process, customization, inspection, packaging, and inquiry videos while preserving supplier-provided facts and separating real footage from illustrative content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, factory videos, audio, prompts, and generated task data may be sent to AI Hive.

Mitigation: Use the skill only with media intended for AI Hive processing and avoid passing unrelated or sensitive files to upload, image, video, or audio arguments.

Risk: The skill requires an AI Hive API key that may be stored locally or supplied through environment or command-line configuration.

Mitigation: Use a dedicated API key where possible, keep the local configuration private, and rotate or revoke the key if it is exposed.

Risk: Generated ecommerce videos can misrepresent supplier capabilities if generated visuals are treated as evidence.

Mitigation: Verify factory scale, equipment, capacity, MOQ, lead time, certifications, customer cases, and other claims against supplier-provided evidence before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/1688-ecommerce-video-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with bash commands; helper commands can return JSON task data and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key and may upload selected images, video, audio, and prompts to AI Hive before downloading generated media.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

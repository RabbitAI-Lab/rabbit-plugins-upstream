## Description:

Seedream 5.0 Lite 图片编辑 helps agents edit authorized images with dependency-ordered queues that lock facts and geometry before object removal, replacement, extension, lighting changes, and finishing through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to create structured Seedream 5.0 Lite image-editing commands for authorized reference images. It is suited for localized object removal, color replacement, outpainting, portrait cleanup, lighting adjustments, product images, ad revisions, and AIGC post-processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to AI Hive for processing.

Mitigation: Use only images the operator is authorized to edit and install only when sharing those inputs with AI Hive is acceptable.

Risk: Generated edits can misrepresent people, news, evidence, brands, product defects, or product claims.

Mitigation: Review outputs carefully, preserve the original image and task record, and disclose substantive edits where needed.

Risk: The helper uses a local AI Hive API key for authenticated requests.

Mitigation: Store the key with restricted local permissions, avoid exposing it in prompts or logs, and rotate it if it may have been shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-image-edit)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; helper commands can emit JSON task details and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires at least one input image, an AI Hive API key, and the fixed public_model_seedream_5_0_lite model.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

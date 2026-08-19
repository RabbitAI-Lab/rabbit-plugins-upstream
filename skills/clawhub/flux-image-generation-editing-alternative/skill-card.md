## Description:

This skill helps agents migrate FLUX-style image generation and editing work to AI Hive Nano Banana Pro while preserving prompt priorities, product accuracy, reference-image roles, and delivery aspect ratios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and content teams use this skill to convert FLUX-oriented image generation or editing requests into AI Hive Nano Banana Pro workflows. It provides prompt-structuring guidance and runnable commands for text-to-image, image-to-image, product advertising, reference-image separation, controlled edits, and candidate generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly selected reference images are sent to AI Hive and object storage.

Mitigation: Use only approved prompts and images for the intended workflow, and avoid uploading confidential or unauthorized material unless the user has accepted that data flow.

Risk: The skill can store an AI Hive API key in ~/.ai-hive/config.json.

Mitigation: Use a dedicated AI Hive API key where possible, keep the config file private, and remove the stored credential when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/flux-image-generation-editing-alternative)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key portal](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; CLI status text, JSON task data, and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts prompts, optional reference images, batch size, routing mode, output directory, and model parameters; generated images default to ~/Downloads/AiHive.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Create and edit Amazon product videos, listing demos, storefront brand clips and advertising video assets using AI Hive text-to-video, image-to-video, reference-to-video, editing, extension and delivery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators and ecommerce content teams use this skill to draft product-first video generation or editing commands for listing demos, setup sequences, feature proof clips, storefront stories, ad variants and localization. It helps preserve product facts from merchant-approved source material while routing media generation through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product media and prompts may be sent to AI Hive, and provider charges may apply.

Mitigation: Use only approved media and prompts, confirm AI Hive terms and pricing before batch production, and avoid uploading assets without usage rights.

Risk: The AI Hive API key may be stored locally in ~/.ai-hive/config.json.

Mitigation: Prefer least-privilege keys where available, keep the local config file restricted to the current user, and rotate keys if exposure is suspected.

Risk: Generated ecommerce videos can contain unsupported product claims, badges, reviews, pricing or marketplace compliance issues.

Mitigation: Base prompts on merchant-approved source material, remove unsupported claims, and manually verify the current Amazon listing and advertising requirements for the target marketplace and category.

Risk: Generated output files may be saved automatically to the default AI Hive downloads directory.

Mitigation: Use --no-download or --output-dir when tighter control over saved outputs is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/amazon-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands; CLI responses are JSON status objects and downloaded media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports task polling, optional no-download mode, configurable output directory and local AI Hive API key configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

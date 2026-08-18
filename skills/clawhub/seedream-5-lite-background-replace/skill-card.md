## Description:

Helps agents replace backgrounds in authorized product or portrait images with Seedream 5.0 Lite while preserving subject identity and matching lighting, perspective, shadows, reflections, and depth of field for ecommerce and marketing assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and ecommerce or marketing teams use this skill to guide AI Hive Seedream 5.0 Lite image-editing workflows for authorized background replacement. It provides prompt patterns and CLI usage for keeping the subject stable while rebuilding scene context, lighting, shadows, reflections, and edge treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts are sent to AI Hive for processing.

Mitigation: Use the skill only with images and prompts that are acceptable to share with AI Hive.

Risk: An AI Hive API key may be stored locally after initialization.

Mitigation: Store the key with restricted file permissions, rotate it if exposed, and avoid entering shared or production keys on untrusted machines.

Risk: Background replacement can misrepresent people, homes, stores, artwork, brands, locations, affiliations, or factual events.

Mitigation: Use only authorized images and review outputs to ensure the edited scene does not imply false endorsement, identity, setting, role, capability, or news context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedream-5-lite-background-replace)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline bash commands and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Seedream 5.0 Lite image model through AI Hive, requires at least one input image, and can save generated images to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

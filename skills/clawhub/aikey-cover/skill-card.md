## Description:

Creates platform-sized video cover images from a person's photo, background image, and topic, with separate layouts and checks for each requested aspect ratio and language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and their agents use this skill to produce and check cover images for selected platforms, including separate Chinese and English versions when requested. It saves images and production notes but does not publish them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personal photos and backgrounds may be shared with an image-generation service or retained in the configured vault.

Mitigation: Use an approved image tool and confirm where source images, finished covers, notes, and skill memory are stored before processing sensitive media.

Risk: Broad cover-related phrases may activate the skill unexpectedly and lead to persistent preference notes.

Mitigation: Review trigger phrases and memory-writing behavior; narrow activation or disable persistent notes where appropriate.

Risk: Generated cover text, faces, dimensions, or platform crops may be incorrect or misleading.

Mitigation: Check wording, subject likeness, actual pixels, and each platform's upload preview before using a cover.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iamzifei/skills/aikey-cover)
- [Platform size guide](references/平台尺寸表.md)
- [Cover design and verification rules](references/规则卡.md)

## Skill Output:

**Output Type(s):** [Image files, Markdown, Guidance]

**Output Format:** [PNG cover images and Markdown production notes; prompts and layout plans if image generation is unavailable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Checks actual image dimensions and files covers by date; does not publish.]

## Skill Version(s):

0.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

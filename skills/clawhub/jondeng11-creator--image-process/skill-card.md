## Description:

A local Pillow-based image processing skill for resizing, converting, compressing, trimming borders, generating thumbnails and OG cards, batch-processing folders, and removing backgrounds without uploading images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jondeng11-creator](https://clawhub.ai/user/jondeng11-creator)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, and developers use this skill to run common local image-processing tasks through an agent, including resize, format conversion, compression, border trimming, thumbnail generation, OG-card creation, batch folder processing, and background removal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing dependencies can execute third-party package code, and optional background removal can download a large model.

Mitigation: Install Pillow and rembg only in a trusted Python environment; use rembg only when background removal is needed and expect the first model download.

Risk: Batch processing can write many derived image files into the selected output folder.

Mitigation: Choose a separate output folder and point the input only at image directories intended for processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jondeng11-creator/skills/image-process)
- [WorkBuddy homepage](https://www.workbuddy.cn)
- [Python downloads](https://www.python.org/downloads/)

## Skill Output:

**Output Type(s):** [Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-selected image files; background removal requires optional rembg setup and may download a model on first use.]

## Skill Version(s):

1.0.0 (source: manifest.yaml and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

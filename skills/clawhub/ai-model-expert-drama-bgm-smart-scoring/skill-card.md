## Description:

Helps short-drama, comic-drama, advertising, ecommerce, and performance-marketing teams organize media into rough cuts, finished edits, platform aspect-ratio variants, audio treatments, and original remixes based on authorized references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative, editing, ecommerce, and marketing teams use this skill to plan short-drama BGM workflows, inspect source media, create rough or finished edits, adapt videos for platform formats, and generate auditable commands or prompts for AI-HIVE and local ffmpeg workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video, image, or audio assets may be uploaded to AI-HIVE when using the generation helpers.

Mitigation: Use only authorized assets and confirm that external upload to AI-HIVE is acceptable for the project before invoking API-backed generation commands.

Risk: The skill requires an AI-HIVE API key for API-backed workflows.

Mitigation: Keep real keys out of shared repositories, screenshots, and public skill files; prefer local environment variables or a protected local config file.

Risk: The included helper scripts cover broader image and video generation behavior than the BGM-focused title alone suggests.

Mitigation: Review the image and video helper scripts and only enable workflows that match the expected media-editing scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-bgm-smart-scoring)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local ffmpeg or ffprobe execution and AI-HIVE API tasks; generated media handling depends on user-provided credentials and authorized assets.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

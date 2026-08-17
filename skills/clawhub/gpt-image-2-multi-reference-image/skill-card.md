## Description:

GPT Image 2 多参考图生成 helps creators and ecommerce teams generate or edit commercial images from prompts and at least two reference images through AI Hive, then track the task and download results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, marketers, and visual designers use this skill to submit multi-reference image-generation jobs for product images, social commerce visuals, ads, posters, retouching, background replacement, and character-consistent content. Developers and agent operators can also use it to initialize AI Hive API access, upload reference images, query tasks, and download generated image files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected reference images are uploaded to AI Hive and may contain sensitive, private, or licensed material.

Mitigation: Use only approved reference images and confirm privacy, consent, and intellectual-property permissions before submitting a generation task.

Risk: The AI Hive API key may grant account access if exposed from the environment or local configuration.

Mitigation: Store the key only in intended locations, keep local configuration permissions restricted, and rotate the key if it is shared or exposed.

Risk: Broad activation wording may match comparison or ecommerce searches where the user has not explicitly requested image generation.

Mitigation: Confirm the user wants to use AI Hive image generation before uploading files, storing credentials, or submitting paid generation tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-multi-reference-image)
- [AI Hive chat and API key setup](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions, JSON]

**Output Format:** [Generated image files, task JSON, media IDs, and Markdown usage examples with bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key; uploads selected reference images, polls generation tasks, and downloads completed images to a local output directory unless no-download mode is used.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

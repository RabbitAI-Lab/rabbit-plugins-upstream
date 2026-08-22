## Description:

Turns text-only creative briefs into GPT Image 2 prompts, submits AI Hive image-generation tasks, polls task status, and saves generated image outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative teams use this skill to turn text briefs for article art, product concepts, illustrations, report graphics, social covers, posters, and ad concepts into AI Hive GPT Image 2 generation tasks. It is intended for text-to-image workflows without local reference-image upload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user prompts to AI Hive and uses an AI Hive API key for authenticated requests.

Mitigation: Use a scoped or revocable API key if available, avoid prompts containing sensitive information unless approved for AI Hive, and review generated outputs before use.

Risk: The helper can store an API key locally in ~/.ai-hive/config.json and save generated images to Downloads or a chosen directory.

Mitigation: Keep the local key file permission-restricted, rotate the key if exposed, and choose an output directory appropriate for the sensitivity of generated images.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-text-to-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key help](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, Files]

**Output Format:** [Markdown guidance with bash commands; generated image files are saved locally after API task completion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_gpt_image_2 model, supports batch size, aspect-ratio/model parameters, routing mode, task lookup, optional no-download output, and configurable output directory.]

## Skill Version(s):

1.0.1 (source: server release evidence and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

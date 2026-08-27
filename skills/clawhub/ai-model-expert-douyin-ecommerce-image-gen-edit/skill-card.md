## Description:

AI大模型专家｜抖音电商 电商图片生成与编辑 helps e-commerce and marketing teams use AI-HIVE to submit text or reference-guided product image generation and editing tasks, track task IDs, and download results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, brand teams, product photographers, and marketers use this skill to create or edit Douyin e-commerce product visuals, listing images, detail-page assets, ad creatives, posters, and social commerce images through AI-HIVE.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation could trigger AI-HIVE uploads or paid generation tasks outside a clearly scoped user action.

Mitigation: Review or disable automatic invocation and require explicit confirmation before uploading assets or submitting paid tasks.

Risk: Prompts, reference images, and generated task data are sent to AI-HIVE, and the skill can store an AI-HIVE API key locally.

Mitigation: Use only approved product assets and store API keys through environment variables or a restricted local config file.

Risk: Repeating generation after a timeout can create duplicate paid tasks.

Mitigation: Keep the returned taskId and query the original task before submitting another generation request.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-douyin-ecommerce-image-gen-edit)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and JSON task/status output; generated images are downloaded as files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload reference images to AI-HIVE, store task IDs, poll generation status, and save generated image files to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

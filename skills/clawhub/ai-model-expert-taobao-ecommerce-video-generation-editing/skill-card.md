## Description:

AI大模型专家｜淘宝 电商视频生成与编辑 helps e-commerce, brand, live-commerce, and creator teams use AI-HIVE to generate, edit, track, and download Taobao-oriented product and marketing videos from text and optional media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, brand product teams, live-commerce teams, and commercial content creators use this skill to create or revise product videos, ads, social commerce clips, short dramas, and other marketing video assets through AI-HIVE. It can submit generation jobs, upload selected reference media, poll task status, and download completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to AI-HIVE during generation or upload workflows.

Mitigation: Use the skill only with media and prompts that are appropriate to send to AI-HIVE, and avoid private or third-party content unless you have rights to use it.

Risk: The AI-HIVE API key may incur charges, especially for batch or high-cost video jobs.

Mitigation: Keep the API key private, review the pricing snapshot before expensive runs, and confirm budget before submitting batches.

Risk: A local timeout does not necessarily mean a submitted generation job failed, and resubmitting may create duplicate paid work.

Mitigation: Save the returned taskId and use the task query workflow to continue checking the original job before submitting another one.

Risk: Generated marketing videos can include incorrect product claims, unauthorized brand elements, or inappropriate impersonation if prompts or references are not reviewed.

Mitigation: Verify product facts, rights to reference materials, trademarks, identities, and final video content before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-taobao-ecommerce-video-generation-editing)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON task/status output; generated video files are downloaded when tasks complete.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI-HIVE API key and may upload user-selected image, video, or audio media before saving generated results to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

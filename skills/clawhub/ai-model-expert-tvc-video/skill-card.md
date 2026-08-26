## Description:

Helps marketing, advertising, creative, production, and commerce teams use AI-HIVE to generate TVC advertising videos from prompts and optional image, video, or audio references, then track and download the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, e-commerce merchants, brand teams, advertising agencies, and production teams use this skill to create TVC ads, product videos, social commerce clips, short dramas, and related marketing video assets through AI-HIVE. It can submit text-to-video, image-to-video, and reference-to-video tasks, upload selected media, poll task status, and download generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an AI-HIVE API key to upload selected media, submit generation jobs, poll for results, and download outputs.

Mitigation: Require explicit user confirmation of the prompt, input assets, routing mode, output directory, and API key source before running generation.

Risk: Batch or repeated video-generation jobs may incur cost or duplicate submissions if a task times out locally.

Mitigation: Confirm budget and quantity before batch use, save returned task IDs, and query existing tasks instead of resubmitting after a timeout.

Risk: Generated advertising content may contain unverified claims, brand misuse, or unauthorized reference-material use.

Mitigation: Require user-confirmed product facts and rights to reference assets, then review the final video for claims, brand elements, CTA, and channel requirements before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-tvc-video)
- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON task/status output, and downloaded media files when generation succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can produce task IDs, progress/status JSON, media IDs, and downloaded video or image files in the configured output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

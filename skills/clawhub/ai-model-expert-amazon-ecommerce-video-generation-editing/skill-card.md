## Description:

This skill helps e-commerce operators, brand teams, livestream commerce teams, and content creators use AI-HIVE to generate, edit, track, and download Amazon-oriented product and marketing videos from text and optional media references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce, brand, advertising, social commerce, and content production users use this skill to prepare prompts and media, submit AI-HIVE video generation or editing tasks, monitor task progress, and retrieve finished video assets for product listings, ads, TVC-style content, short drama, and social media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires an AI-HIVE API key and may store it in a local configuration file.

Mitigation: Prefer an environment variable for temporary use, keep any local config file private, and revoke the AI-HIVE key when it is no longer needed.

Risk: Selected images, videos, or audio files are uploaded to AI-HIVE for generation or editing.

Mitigation: Upload only media the user is permitted to process and avoid sensitive or confidential assets unless AI-HIVE handling is acceptable.

Risk: Generation jobs may incur cost, and repeating timed-out submissions can create duplicate paid tasks.

Mitigation: Review the runtime pricing snapshot, confirm budget before bulk work, save taskId values, and poll existing tasks instead of resubmitting after timeouts.

Risk: Generated product, brand, or advertising content can contain inaccurate claims or rights-sensitive elements.

Mitigation: Verify product facts, usage rights, trademarks, and platform requirements before publishing generated video outputs.

## Reference(s):

- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-amazon-ecommerce-video-generation-editing)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with command examples, configuration instructions, JSON task responses, and downloaded video or image files when the helper script is executed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper script can upload selected media, submit AI-HIVE jobs, return taskId values, poll task status, and save generated results to a local output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

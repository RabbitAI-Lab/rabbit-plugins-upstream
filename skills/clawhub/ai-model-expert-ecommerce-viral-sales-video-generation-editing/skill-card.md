## Description:

AI-HIVE skill for generating and editing e-commerce sales videos from text and optional media, with task submission, polling, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, brand teams, livestream commerce teams, marketers, and content creators use this skill to create or edit product, advertising, TVC, social commerce, and short-form video assets through AI-HIVE. The skill can upload selected source media, submit generation jobs, preserve task IDs, poll progress, and download completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload selected image, video, or audio files to AI-HIVE and submit remote generation jobs.

Mitigation: Require explicit user confirmation before uploading media or submitting a task, especially when the request is ambiguous or involves commercial assets.

Risk: Remote generation jobs may incur charges, particularly for batches or high-cost routing choices.

Mitigation: Confirm budget, task count, routing mode, and the current pricing snapshot before submitting paid or batch work.

Risk: The workflow requires an AI-HIVE API key that may be stored locally.

Mitigation: Use environment variables or a locked-down local config file, avoid exposing real keys in chats or repositories, and rotate credentials if disclosure is suspected.

## Reference(s):

- [AI-HIVE entry point](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-ecommerce-viral-sales-video-generation-editing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Files]

**Output Format:** [Markdown guidance with shell commands, JSON task responses, and downloaded video or image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AI-HIVE API credentials, optional local media inputs, remote task IDs, polling status, and a configurable output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

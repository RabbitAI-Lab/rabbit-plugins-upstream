## Description:

Seedance 2.5 Image-to-Video helps creators, marketers, ecommerce teams, and short-form video producers provide a first-frame image and motion prompt, submit an AI Hive video generation task, track progress, and download the finished video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketing teams, ecommerce operators, and video production teams use this skill to turn a supplied image and prompt into short AI-generated video assets for ads, product showcases, social media, short drama, and comic-style video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the trigger scope is broader than the side-effectful upload, credential, billing, and API actions the skill can perform.

Mitigation: Use the skill only after an explicit user request to upload selected media and submit a Seedance 2.5 image-to-video task; avoid operational generation for broad competitor, ecommerce, or pricing research prompts.

Risk: The skill requires an AI Hive API key and may store credentials for later use.

Mitigation: Store the API key in an environment variable or the documented config file with restricted permissions, avoid logging secrets, and rotate or revoke keys that may have been exposed.

Risk: Generated tasks can incur costs, and repeated submissions may duplicate billing.

Mitigation: Review task count and routing before submission, keep returned task IDs, use task status checks for pending work, and monitor generated-task costs.

Risk: Media files selected by the user are uploaded to AI Hive for processing.

Mitigation: Upload only files the user intentionally selected for generation and avoid sending confidential or policy-restricted media unless the deployment has approved that use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-2-5-image-to-video)
- [AI Hive chat and API key entry](https://ai-hive.iclip.cn/chat)
- [AI Hive OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, the bundled script can upload selected media, submit AI Hive generation tasks, poll task status, and download generated video files.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata; artifact changelog top entry is 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

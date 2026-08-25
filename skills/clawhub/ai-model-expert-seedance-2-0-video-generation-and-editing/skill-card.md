## Description:

Helps agents use AI-HIVE to submit Seedance2.0 text-to-video, image-to-video, and reference-guided video generation tasks, manage media uploads, poll task status, and download finished videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, advertising teams, and video production teams use this skill to create AI-generated product, advertising, TVC, social, short drama, and comic-style videos through AI-HIVE. Developers and operators can also use it to configure API access, upload reference media, submit generation jobs, preserve task IDs, and download results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload user-selected prompts and media to AI-HIVE.

Mitigation: Use explicit invocation, confirm which media will be uploaded, and avoid sensitive or proprietary material unless AI-HIVE retention and usage terms are acceptable.

Risk: The workflow stores or reads an AI-HIVE API key locally.

Mitigation: Keep API keys out of public files and logs, store local configuration with restrictive permissions, and rotate keys if exposure is suspected.

Risk: Video generation jobs may incur charges and broad implicit invocation is enabled.

Mitigation: Confirm before high-cost or batch runs, review the live pricing snapshot, and preserve task IDs instead of resubmitting timed-out jobs.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-seedance-2-0-video-generation-and-editing)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit remote AI-HIVE jobs, upload selected media, return task IDs, and download generated video files when configured with an API key.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

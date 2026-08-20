## Description:

Helps video editors, post-production teams, ad producers, e-commerce operators, and creators generate or edit videos from text plus optional image, video, or audio references through AI Hive, with task submission, progress checks, and result downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, video production teams, and e-commerce operators use this skill to generate, edit, extend, and repurpose video assets for ads, product displays, social content, short dramas, and marketing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to AI Hive for processing.

Mitigation: Use only prompts and media approved for AI Hive processing, and avoid submitting sensitive or unlicensed material unless that use is permitted.

Risk: The skill requires an AI Hive API key and can store it in `~/.ai-hive/config.json`.

Mitigation: Protect the API key, keep the config file private, rotate exposed keys, and use the default AI Hive base URL unless another endpoint is intentionally trusted.

Risk: Video generation may incur cost, and resubmitting after a local timeout could duplicate work.

Mitigation: Check real-time pricing before large batches, keep returned task IDs, and use task status lookup instead of resubmitting timed-out jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/video-generation-and-editing)
- [AI Hive API access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with shell commands, JSON task/status responses, and downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include task IDs, progress/status JSON, and MP4/MOV video files saved to the configured output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

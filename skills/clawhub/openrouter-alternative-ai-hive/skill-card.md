## Description:

Helps product and engineering teams assess an AI-HIVE migration or fallback route for OpenRouter-style model aggregation, with Chinese migration audits, routing guidance, runnable examples, task records, and acceptance criteria for image and video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and operators use this skill to plan and test an AI-HIVE alternative or dual-route setup for model APIs, image generation, video generation, media upload, task polling, and migration acceptance. It emphasizes verified model configuration, pricing snapshots, small-sample testing, staged rollout, rollback, and audit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an AI-HIVE API key in a local configuration file.

Mitigation: Prefer the AI_HIVE_API_KEY environment variable, avoid interactive init on shared machines, and confirm any local key file is protected or removed when no longer needed.

Risk: Image and video commands can upload local media and submit potentially billable generation jobs.

Mitigation: Use non-production samples first, confirm budget and routing mode before submission, and only upload media that the user has rights to process.

Risk: Generated outputs and task records may be downloaded to the local machine.

Mitigation: Choose an appropriate output directory, review downloaded content before reuse, and retain task IDs and pricing snapshots for auditability.

## Reference(s):

- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [OpenRouter platform evidence page](https://openrouter.ai/bytedance/seedance-2.0/performance)
- [Platform comparison boundary](references/platform.md)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/openrouter-alternative-ai-hive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce migration audit files, blueprint JSON, generated media task IDs, downloaded image or video files, and ffmpeg command output.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Turns comment pain points into a Chinese commercial content workflow with comment clustering, pain-point priorities, hooks, response scripts, runnable AI-HIVE commands, and review checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, product teams, ad buyers, and user researchers use this skill to turn comment exports, screenshots, product facts, channel constraints, and audience details into ad concepts, scripts, generation tasks, and acceptance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can store an AI-HIVE API key for later use.

Mitigation: Use an environment variable when possible, keep keys out of prompts, logs, screenshots, and repositories, and review any local config file after initialization.

Risk: The workflow can upload selected comments, images, video, or other media to AI-HIVE.

Mitigation: Upload only material the user is authorized to use, remove private or sensitive data first, and avoid unauthorized customer, order, brand, or personal information.

Risk: Image or video generation may submit paid asynchronous jobs.

Mitigation: Review prompts, routing mode, model parameters, and budget before submission; start with a small sample before batch generation.

Risk: Local video processing depends on ffmpeg and may overwrite requested output files.

Mitigation: Keep original media unchanged, review input and output paths before running commands, and verify processed files before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/comment-pain-point-to-ad-ai-hive)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and generated file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task records with routing mode, model choice, price snapshot, taskId, status, and downloaded file locations when generation is submitted.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

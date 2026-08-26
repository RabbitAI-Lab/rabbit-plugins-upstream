## Description:

Helps creators, merchants, and marketers turn authorized still images into Seedance and AI-HIVE video production plans, prompts, runnable commands, task records, and acceptance checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing teams use this skill to plan and execute image-to-video workflows for ecommerce, advertising, social video, and short-form content. It emphasizes authorized source media, stable product or subject appearance, reviewable prompts, AI-HIVE task execution, and delivery checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images, videos, or audio may be uploaded to AI-HIVE for generation.

Mitigation: Use only media the user is authorized to process, and confirm the final inputs before submitting any generation task.

Risk: Approved generation tasks may incur AI-HIVE costs.

Mitigation: Review model configuration, routing mode, and pricing snapshot before execution; start with a small sample for batch work.

Risk: An AI-HIVE API key may be stored locally in ~/.ai-hive/config.json.

Mitigation: Prefer environment variables when practical, avoid exposing keys in chats or logs, keep the config file permission-restricted, and remove the file when the credential is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/seedance-image-to-video-studio-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured checklists, prompts, task records, JSON files, and inline shell or Python commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit AI-HIVE generation tasks after user approval, poll asynchronous task status, and download generated media to a local output directory.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

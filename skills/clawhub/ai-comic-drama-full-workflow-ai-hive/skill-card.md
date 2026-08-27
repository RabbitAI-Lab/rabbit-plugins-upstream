## Description:

Turns AI comic-drama production requests into a production-ready Chinese workflow with scripts, prompts, shot lists, AI-HIVE generation commands, task records, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, comic-drama studios, short-video teams, novel IP owners, ecommerce marketers, and independent creators use this skill to turn story, style, character, platform, duration, and budget inputs into an auditable AI comic-drama production plan and runnable generation workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit AI-HIVE media generation jobs that may incur cost, especially for batch jobs.

Mitigation: Review prompts, routing mode, model choice, uploaded media, and estimated cost before running generate commands; start with a small sample before batch generation.

Risk: Reference images, videos, or audio selected by the user may be uploaded to AI-HIVE.

Mitigation: Upload only media the user is authorized to use and avoid sensitive, private, or restricted content unless appropriate permissions and policies are confirmed.

Risk: An API key may be stored locally for convenience.

Mitigation: Use environment variables or the provided local config flow, keep the key out of scripts, logs, screenshots, and version control, and maintain restrictive file permissions.

## Reference(s):

- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-comic-drama-full-workflow-ai-hive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with runnable bash commands, Python helper scripts, JSON task records, and Chinese production checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE APIs, upload user-selected media, store a local API key configuration, poll asynchronous generation tasks, download generated media, and run ffmpeg for deterministic video edits.]

## Skill Version(s):

1.0.0 (source: server release evidence, created 2026-08-24T14:58:42Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps advertising and marketing teams create Chinese image, short-video, and content-marketing plans with audience strategy, 30-day calendars, prompts, platform rewrites, AI-HIVE task records, and review checkpoints for authorized assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, creators, and agency teams use this skill to plan and produce advertising-company image, short-video, and content-marketing assets for Chinese social and private-domain channels. It emphasizes fact checks, authorized materials, budget confirmation, AI-HIVE task tracking, and post-campaign review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation and media uploads may trigger billable external API activity.

Mitigation: Confirm budget, model route, materials, and task parameters before starting generation or upload tasks.

Risk: API keys can be exposed through logs, screenshots, shared files, or committed configuration.

Mitigation: Keep AI_HIVE_API_KEY in environment variables or protected local configuration and avoid sharing generated logs or files containing credentials.

Risk: Uploaded images, videos, logos, music, people, or customer examples may lack sufficient usage rights.

Mitigation: Upload only materials the user has rights to use and mark uncertain facts or assets for review before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/industry-advertising-agency-marketing-ai-hive)
- [Publisher Profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API](https://ai-hive.iclip.cn/api)
- [Advertising image and video content marketing playbook](references/industry-playbook.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, Python helper usage, and JSON task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate AI-HIVE API uploads, generation tasks, polling, downloads, and local ffmpeg edits when the user confirms materials, budget, and routing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

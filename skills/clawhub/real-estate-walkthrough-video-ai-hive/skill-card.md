## Description:

Helps agents turn authorized real-estate showroom or property media into a Chinese AI-HIVE video production workflow with shot plans, prompts, runnable API commands, generated video tasks, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External real-estate marketing, home decor, homestay, and space-design teams use this skill to plan and execute authorized showroom walkthrough videos for commercial and social platforms. It guides the agent through input review, shot planning, AI-HIVE generation commands, task tracking, and delivery acceptance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE generation calls can require API credentials and may incur costs.

Mitigation: Review prompts, routing, model parameters, uploaded media, and output paths before running commands; run small samples before batch jobs.

Risk: Property media, layouts, area, lighting, facilities, and views can be misleading if source facts or rights are not verified.

Mitigation: Use only authorized property and media assets, mark unverified facts for review, and do not treat generated walkthroughs as measurement or real-viewing substitutes.

Risk: Custom API endpoints or unsafe credential handling can expose API keys or uploaded media.

Mitigation: Keep API keys out of prompts, logs, screenshots, and repos; avoid custom AI_HIVE_BASE_URL values unless the endpoint is explicitly trusted.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wubin1836/skills/real-estate-walkthrough-video-ai-hive)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local project blueprints, media task records, downloaded generation outputs, and deterministic ffmpeg edit commands.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

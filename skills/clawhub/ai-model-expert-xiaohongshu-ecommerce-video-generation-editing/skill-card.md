## Description:

Helps ecommerce operators, brand teams, livestream commerce teams, and commercial creators generate or edit Xiaohongshu-focused product videos through AI-HIVE using text prompts and optional image, video, or audio references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to submit, track, and download AI-HIVE video generation or editing jobs for ecommerce ads, product showcases, Xiaohongshu seeding content, short drama, and social commerce assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports broad automatic invocation scope for a skill that can upload media and submit paid AI-HIVE jobs.

Mitigation: Before execution, confirm the exact media files, expected cost or routing mode, output directory, and whether a job should be submitted.

Risk: The skill uses an AI-HIVE API key and may store it in local configuration.

Mitigation: Treat the API key as a credential, keep it out of public artifacts and chat logs, and prefer narrow invocation for relevant video-generation tasks only.

Risk: Repeated submissions after a local timeout may create duplicate paid jobs.

Mitigation: Save the returned task ID and poll the original task instead of resubmitting unless the user explicitly approves a new job.

Risk: Reference media, brand elements, product claims, or likenesses may create rights, impersonation, or misleading-advertising issues.

Mitigation: Use only authorized reference materials and require user-confirmed product facts, permissions, brand assets, claims, and identity details before generation.

## Reference(s):

- [AI-HIVE Chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base](https://ai-hive.iclip.cn/api)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-model-expert-xiaohongshu-ecommerce-video-generation-editing)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can submit AI-HIVE jobs, return task IDs, poll status, upload media, and download generated video files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

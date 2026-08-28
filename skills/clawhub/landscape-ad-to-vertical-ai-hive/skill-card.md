## Description:

Helps brands and merchants convert authorized 16:9 ads, TVCs, and launch footage into reviewable 9:16 short-video workflows with editing commands, AI-HIVE generation options, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing teams use this skill to plan and execute authorized landscape-to-vertical ad reconstruction for ecommerce, social, and short-video campaigns. Developers can also use its helper scripts for local media probing, deterministic ffmpeg edits, AI-HIVE media upload, task submission, polling, and output download.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can submit paid AI-HIVE generation jobs or upload user-provided media.

Mitigation: Review prompts, routing mode, model configuration, price snapshots, and uploaded files before running generation; use small samples for batch work.

Risk: API keys or uploaded media could be exposed through shared logs, screenshots, repositories, or weak local configuration handling.

Mitigation: Keep AI_HIVE_API_KEY out of shared logs and repositories, use placeholder keys in examples, and store local configuration with restricted permissions.

Risk: Ad reconstruction can create copyright, trademark, endorsement, platform-policy, or factual-claim issues if source material is unauthorized or claims are not verified.

Mitigation: Use only authorized assets, avoid copying protected expression or misleading endorsements, mark unverifiable facts for review, and keep required disclosures and brand constraints intact.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/landscape-ad-to-vertical-ai-hive)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Files, API Calls, Guidance]

**Output Format:** [Markdown with JSON files, shell commands, generated media files, and task-status records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize reviewable plans before paid generation, preserve original files, and may write local blueprint JSON or downloaded AI-HIVE media results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

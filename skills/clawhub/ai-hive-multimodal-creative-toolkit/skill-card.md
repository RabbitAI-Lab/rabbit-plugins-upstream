## Description:

AI-HIVE 多模态创意工具箱 helps ecommerce, advertising, short-video, social media, and AI application teams turn creative requests into reviewable workflows, runnable AI-HIVE commands, prompts, task records, and local image or video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce operators, and developers use this skill to plan AI-HIVE image and video projects, choose cost, speed, or success routing, run API-backed generation or ffmpeg editing commands, and track outputs for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API calls can incur generation charges, especially for video or batch jobs.

Mitigation: Review final prompts, model routing, pricing snapshot, and batch size before submitting paid generation tasks; run a small sample before scaling.

Risk: Reference images or videos are uploaded to AI-HIVE when explicitly supplied to generation commands.

Mitigation: Use only media the user is authorized to process, and avoid passing private or sensitive files unless upload is intended and approved.

Risk: API keys may be exposed if stored in shared environments, logs, screenshots, or committed files.

Mitigation: Use environment variables or the documented local configuration flow, keep placeholder keys in examples, and avoid storing real keys in shared repositories.

Risk: Generated commercial claims, product facts, platform rules, prices, and model availability can become inaccurate or misleading.

Mitigation: Keep factual claims grounded in user-provided evidence or current AI-HIVE responses, and require human review before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-multimodal-creative-toolkit)
- [AI-HIVE Chat and API Access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API Base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON project briefs, Python command output, and downloaded media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local blueprint JSON files, save generated media under the configured output directory, and print AI-HIVE task identifiers and status records.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

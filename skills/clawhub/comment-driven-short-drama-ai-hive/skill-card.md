## Description:

Turns audience-comment-driven short drama requests into reviewable Chinese production workflows, script and storyboard materials, runnable AI-HIVE commands, generation task records, and continuity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, short-drama teams, brand IP teams, and community operators use this skill to convert prior episodes, character and scene bibles, audience comments, platform constraints, and authorized media into a next-episode production plan. Developers and operators can also use its bundled scripts to create blueprints, call AI-HIVE image or video generation, upload authorized media, poll tasks, download results, and perform deterministic ffmpeg edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key and can store credentials for later command-line use.

Mitigation: Use environment variables or the generated config file with restricted permissions, and avoid placing API keys in logs, screenshots, repositories, or shared prompts.

Risk: Generation commands can upload user-selected media and may incur paid image or video generation costs.

Mitigation: Review prompts, model routing, parameters, and authorized input files before submitting generation jobs; run small samples before batch work.

Risk: Audience comments, reference materials, product claims, or brand assets may introduce privacy, copyright, trademark, or truthfulness issues.

Mitigation: Use only authorized media, remove private commenter details, mark unverifiable claims as needing validation, and keep human review before publication.

Risk: Generated short-drama output may drift from character continuity, product facts, platform rules, or campaign goals.

Mitigation: Use the skill's acceptance checklist for continuity, factual claims, routing records, task IDs, and risk review before final delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/comment-driven-short-drama-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API endpoint](https://ai-hive.iclip.cn/api)
- [Publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline bash commands, JSON task records, generated media files, and concise review checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid AI-HIVE image or video generation tasks after user review; local video edits require ffmpeg.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

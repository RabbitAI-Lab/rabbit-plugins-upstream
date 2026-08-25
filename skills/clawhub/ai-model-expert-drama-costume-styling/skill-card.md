## Description:

AI大模型专家｜短剧服装造型设定 helps short-drama, comic, brand, e-commerce, acquisition, and international teams turn character, scene, story, and brand requirements into reusable costume-styling visual assets and follow-on video generation workflows through AI-HIVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External short-drama studios, comic creators, brand marketers, e-commerce teams, media buyers, and localization teams use this skill to plan costume styling, create reusable character and scene boards, manage prompt and reference-asset versions, and generate executable AI-HIVE image or video commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an AI-HIVE API key as a real credential.

Mitigation: Keep the key local, avoid committing it to public files or screenshots, and rotate or revoke it if exposure is suspected.

Risk: Prompts and media files may be uploaded for image or video generation.

Mitigation: Review prompts and files before upload and use only materials the user is authorized to process.

Risk: Media generation can incur usage costs or duplicate charges if timed-out tasks are resubmitted.

Mitigation: Check model pricing and task counts before bulk generation, preserve task IDs, and query existing tasks before creating replacements.

Risk: Implicit invocation could cause external AI-HIVE API use without a separate visible command decision.

Mitigation: Disable implicit invocation or require explicit confirmation when every external API call should be approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-drama-costume-styling)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON file outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local project blueprints and AI-HIVE image or video task outputs; API access requires a user-provided AI-HIVE API key.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

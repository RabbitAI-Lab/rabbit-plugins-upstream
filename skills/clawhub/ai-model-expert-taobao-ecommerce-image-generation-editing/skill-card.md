## Description:

AI-HIVE skill for generating and editing Taobao ecommerce images from prompts and optional reference images, with automated media upload, task submission, progress polling, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, brand teams, product photographers, livestream commerce teams, and content creators use this skill to create product main images, detail-page visuals, advertising key visuals, posters, social commerce images, retouching, background replacement, and visually consistent marketing assets through AI-HIVE.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be sent to AI-HIVE during generation.

Mitigation: Use only assets the user is allowed to upload, avoid sensitive material, and confirm data-sharing expectations before submitting jobs.

Risk: Implicit invocation may upload media or start paid external generation tasks.

Mitigation: Require explicit user confirmation of the prompt, route, model, pricing snapshot, and reference assets before task submission.

Risk: The skill can store an AI-HIVE API key in ~/.ai-hive/config.json.

Mitigation: Keep the config file private, do not commit API keys, and prefer environment variables or least-privilege keys where possible.

Risk: Repeated submissions after timeouts may create duplicate paid tasks.

Mitigation: Preserve task IDs and poll existing tasks before creating replacement jobs.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-taobao-ecommerce-image-generation-editing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and generated image files downloaded from AI-HIVE tasks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save API configuration under ~/.ai-hive/config.json and generated outputs under ~/Downloads/AiHive unless overridden.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

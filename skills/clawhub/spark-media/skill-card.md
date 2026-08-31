## Description:

Spark Media helps agents generate and edit images, create text-to-video or image-to-video media, and query media task status using a configured SPARK_MEDIA_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide agents through AI media generation workflows for advertising images, product images, posters, and short video assets. The skill covers API key setup, HTTP request construction, idempotent retries, task polling, and safe handling of prompts, images, media results, and billing signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional images are sent to the ai-skills.open-idea.net external service.

Mitigation: Confirm the service is trusted for the intended content, avoid sensitive images unless necessary and authorized, and disclose this external processing path to users where appropriate.

Risk: API keys could be exposed if copied into chat, logs, generated files, or code examples.

Mitigation: Configure SPARK_MEDIA_API_KEY only as an environment variable and do not ask users to paste full keys into conversation.

Risk: Retries or parallel video creation can duplicate work, create billing ambiguity, or conflict with the one-active-video-task limit.

Mitigation: Use unique Idempotency-Key values per logical request, reuse the same key for retries, follow Retry-After or bounded backoff, and poll existing video tasks instead of submitting parallel replacements.

## Reference(s):

- [Spark Media ClawHub listing](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills platform homepage](https://ai-skills.open-idea.net)
- [API Key configuration](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- [Image generation and editing](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- [Video generation and polling](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/spark-media/BEHAVIOR-RULES.md)
- [Local API key reference](references/API-KEY.md)
- [Local image generation reference](references/IMAGE-GENERATION.md)
- [Local video generation reference](references/VIDEO-GENERATION.md)
- [Local HTTP requests reference](references/HTTP-REQUESTS.md)
- [Local behavior and retry reference](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell, HTTP, JSON, and task-status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SPARK_MEDIA_API_KEY and optional AI_SKILLS_API_URL; image and video creation requests require Idempotency-Key values; video tasks are polled until terminal status.]

## Skill Version(s):

2.4.1 (source: server release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

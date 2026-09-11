## Description:

Spark Media helps agents generate and edit images, create text-to-video or image-to-video media, make short video assets, and check media task status using a configured Spark Media API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to integrate Spark Media image and video generation into agent workflows, including prompt-based generation, reference-image editing, video task polling, and API key configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media prompts and supplied reference images are sent to the Spark Media service.

Mitigation: Use the skill only when users are comfortable sharing those inputs with the service, and obtain consent before uploading sensitive images.

Risk: The skill requires a Spark Media API key stored in OpenClaw configuration.

Mitigation: Store SPARK_MEDIA_API_KEY only in configuration or environment variables, and avoid placing full keys in chats, prompts, logs, source code, or generated files.

Risk: Documentation is primarily Chinese, which may cause misunderstandings for users who cannot read Chinese.

Mitigation: Provide translated documentation or have a bilingual reviewer confirm usage, error handling, and billing behavior before deployment.

Risk: Failed or ambiguous generation jobs can lead to duplicate work or unexpected billing if retried incorrectly.

Mitigation: Reuse idempotency keys for retries of the same request, stop on indeterminate idempotency results, and check task and billing status before submitting new jobs.

## Reference(s):

- [Spark Media Skill Page](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- [Image Generation and Editing](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- [Video Generation and Polling](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- [HTTP Request Examples](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, HTTP request examples, and API configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SPARK_MEDIA_API_KEY; image and video requests send prompts and optional reference images to the Spark Media service.]

## Skill Version(s):

2.5.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Spark Media helps agents generate and edit images, create text-to-video or image-to-video media, produce short video assets, and query media task status through the AI Skills platform API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route AI image and video generation, reference-image editing, short media creation, and media task status checks through the Spark Media API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, reference images, and generated media task data are sent to the Spark Media service.

Mitigation: Use the skill only for intended Spark Media workflows, avoid sensitive images or prompts without consent, and disclose external processing where appropriate.

Risk: The skill requires a Spark Media API key.

Mitigation: Use a scoped API key and keep it out of chats, generated files, logs, and source code.

Risk: Image or video generation requests may incur charges and can be affected by retries or uncertain task state.

Mitigation: Reuse the original idempotency key when retrying 429 or 503 responses, stop on indeterminate idempotency results, and verify task and billing status before submitting replacement jobs.

Risk: Media generation or editing can produce harmful, unlawful, misleading, or privacy-invasive content.

Mitigation: Do not generate unlawful or harmful content, verify authorization before sensitive edits involving real people, and report missing or malformed result fields instead of fabricating media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- [Image generation and editing](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- [Video generation and polling](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](https://ai-skills.open-idea.net/skill-docs/spark-media/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and JSON HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task identifiers, status summaries, billing-header interpretation, and saved media references; requires SPARK_MEDIA_API_KEY.]

## Skill Version(s):

2.5.2 (source: ClawHub release metadata and skill metadata.packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

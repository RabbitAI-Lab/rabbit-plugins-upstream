## Description:

Spark Media helps agents generate and edit images, create text-to-video and image-to-video media, and query media task results through the Spark Media API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Spark Media to create or edit visual media through a configured Spark Media API account. The skill is useful when an agent needs to prepare image or video requests, poll asynchronous video jobs, preserve returned media, and report billing information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied reference images are sent to a remote Spark Media API.

Mitigation: Use the skill only for media you are allowed to process externally, avoid sensitive images unless necessary, and confirm authorization before editing real-person imagery.

Risk: The skill requires a dedicated API key and could expose credentials if copied into prompts, logs, or generated files.

Mitigation: Store SPARK_MEDIA_API_KEY in the environment, do not paste the full key in chat, and avoid writing it into code, prompts, logs, or output files.

Risk: Media generation may incur account charges and video jobs are asynchronous.

Mitigation: Review billing headers, use idempotency keys for creation requests, and poll video tasks with bounded retries until a terminal status is reached.

## Reference(s):

- [Spark Media on ClawHub](https://clawhub.ai/youteacher/skills/spark-media)
- [Spark Media homepage](https://ai-skills.open-idea.net)
- [API Key configuration](references/API-KEY.md)
- [Image generation and editing](references/IMAGE-GENERATION.md)
- [Video generation and polling](references/VIDEO-GENERATION.md)
- [HTTP request examples](references/HTTP-REQUESTS.md)
- [Behavior, errors, and retry rules](references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request examples, and returned media links or saved media files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SPARK_MEDIA_API_KEY; video jobs are asynchronous and require polling until success, failure, or timeout.]

## Skill Version(s):

2.0.0 (source: release evidence and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

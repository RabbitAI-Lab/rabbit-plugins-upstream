## Description:

Helps users generate and edit images, create videos, and check media task progress through the AI Skills Spark Media service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to produce advertising images, product visuals, posters, and short videos from prompts or reference images, and to track video generation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the AI Skills service.

Mitigation: Obtain consent before uploading sensitive material and share only content needed for the task.

Risk: API credentials may be exposed if shared in chat or saved in output.

Mitigation: Configure a dedicated API key where possible and never paste or log the full key.

Risk: Video or batch requests may incur charges or duplicate work on retry.

Mitigation: Review billing before submission, reuse the original idempotency key on retries, and check uncertain tasks before resubmitting.

## Reference(s):

- [Spark Media ClawHub release](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills platform](https://ai-skills.open-idea.net)
- [API key configuration](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- [Image generation and editing](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- [Video generation and task polling](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- [HTTP request examples](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- [Behavior and retry rules](https://ai-skills.open-idea.net/skill-docs/spark-media/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Text, Media links, Shell commands, Configuration guidance]

**Output Format:** [Markdown with media results and task status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation is asynchronous; report task status and any partial failures.]

## Skill Version(s):

2.7.0 (source: ClawHub release and package metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

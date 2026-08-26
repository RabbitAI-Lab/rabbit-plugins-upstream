## Description:

Spark Media helps agents generate and edit images, create text-to-video or image-to-video media, and query media task status using a Spark Media API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request generated or edited images, create short video assets, and check asynchronous media generation results. It is suited for advertising images, product visuals, posters, and short-form media materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to the Spark Media API.

Mitigation: Avoid uploading sensitive or private images unless consent is confirmed and the endpoint is trusted.

Risk: The skill requires SPARK_MEDIA_API_KEY for authenticated API calls.

Mitigation: Keep the API key out of chats, code, logs, prompts, and generated files.

Risk: Media generation may incur usage charges.

Mitigation: Confirm cost-sensitive requests and review billing headers or account balance when charges are relevant.

Risk: Retries or duplicate create requests can create unintended media tasks.

Mitigation: Use a unique Idempotency-Key for each logical creation request and reuse it for retries of the same request.

## Reference(s):

- [Spark Media Skill Page](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](artifact/references/API-KEY.md)
- [Image Generation and Editing](artifact/references/IMAGE-GENERATION.md)
- [Video Generation and Polling](artifact/references/VIDEO-GENERATION.md)
- [Behavior, Errors, and Retry Rules](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API request examples, task status summaries, and media result references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return or save generated media results; avoids printing full base64 data URLs.]

## Skill Version(s):

2.2.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

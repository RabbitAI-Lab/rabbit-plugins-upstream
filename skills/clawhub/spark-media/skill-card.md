## Description:

Spark Media helps agents generate images and videos from prompts, edit or animate reference images, create short media assets, and query media task status using SPARK_MEDIA_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create advertising images, product images, posters, short videos, and other media assets through the Spark Media service. It is also used to poll media generation tasks and retrieve completed results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses SPARK_MEDIA_API_KEY to call an external Spark Media API, so leaked credentials could allow unauthorized generation requests or account charges.

Mitigation: Store SPARK_MEDIA_API_KEY only as a secret environment variable, do not paste full keys into chat, code, logs, prompts, or generated files, and verify AI_SKILLS_API_URL points to the intended endpoint.

Risk: Prompts and reference images may be uploaded to the Spark Media service, including sensitive or user-provided image content.

Mitigation: Upload only content needed for the task, obtain consent before sensitive image uploads or edits involving real people, and avoid unlawful, harmful, or privacy-invasive media generation.

Risk: Generation calls may consume account balance, and retries or duplicate submissions can create unintended costs.

Mitigation: Use a unique Idempotency-Key for each new logical request, reuse the same key for retries, follow Retry-After or bounded backoff, and stop automatic retries when idempotency or billing state is indeterminate.

Risk: Media task responses may be missing fields, fail decoding, or have unknown status.

Mitigation: Report abnormal responses clearly, do not fabricate media outputs, and rely on returned result fields and billing records instead of assumptions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/spark-media)
- [AI Skills Platform](https://ai-skills.open-idea.net)
- [API Key Configuration](artifact/references/API-KEY.md)
- [Image Generation and Editing](artifact/references/IMAGE-GENERATION.md)
- [Video Generation and Polling](artifact/references/VIDEO-GENERATION.md)
- [HTTP Request Examples](artifact/references/HTTP-REQUESTS.md)
- [Behavior, Errors, and Retry Rules](artifact/references/BEHAVIOR-RULES.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands, HTTP request examples, and media task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to submit prompts or reference images to an external media generation service and poll asynchronous video tasks.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill metadata packageVersion)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

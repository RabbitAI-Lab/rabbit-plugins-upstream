## Description: <br>
Spark Media helps an agent generate images from text, generate images from text plus a reference image, create text-to-video or image-to-video tasks, and query asynchronous video results using a Spark Media API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youteacherasia](https://clawhub.ai/user/youteacherasia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request paid image and video generation through Spark Media, including marketing images, reference-image variations, short video prototypes, and follow-up video task status checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and reference images are sent to Spark Media and its upstream provider. <br>
Mitigation: Avoid sensitive or confidential media and tell users before submitting prompts or reference images. <br>
Risk: Image and video requests can spend account credit. <br>
Mitigation: Confirm billed generation requests before execution and show the charged amount and remaining balance after successful calls. <br>
Risk: Video generation is asynchronous and can leave tasks in submitted or processing states. <br>
Mitigation: Return the task ID and current status, then query later until the task succeeds or fails. <br>
Risk: Retrying paid or rate-limited requests incorrectly can cause confusion or duplicate work. <br>
Mitigation: Use idempotency keys for image retries, distinguish daily spending limits from per-minute rate limits, and avoid resubmitting active video tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/youteacherasia/skills/spark-media) <br>
- [Spark Media homepage](https://media.open-idea.net) <br>
- [API key configuration](references/API-KEY.md) <br>
- [Behavior rules](references/BEHAVIOR-RULES.md) <br>
- [HTTP request examples](references/HTTP-REQUESTS.md) <br>
- [Image generation details](references/IMAGE-GENERATION.md) <br>
- [Video task details](references/VIDEO-GENERATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples, status summaries, generated media links or files, and billing lines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Image results may include PNG files or display links; video generation returns task status first and media links after the asynchronous task succeeds.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>

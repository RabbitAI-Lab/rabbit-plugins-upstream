## Description:

Generate or edit AI images with Pixmind for text-to-image, image-to-image, posters, product visuals, covers, and consistent-character work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fuyunzhishang](https://clawhub.ai/user/fuyunzhishang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route Pixmind image generation or editing requests to an appropriate model, submit approved paid generation tasks, poll task status, and return generated image attachments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference image URLs are sent to Pixmind for generation or editing.

Mitigation: Review prompts and reference images for sensitive content before submission, and disclose provider transfer to users when appropriate.

Risk: Pixmind generation may consume paid credits.

Mitigation: Summarize the final prompt, model, ratio, quality or resolution, and count, then obtain approval before submitting a paid task.

Risk: Pixmind API credentials could be exposed if handled in chat or command arguments.

Mitigation: Keep the API key in host credential settings or environment variables and never ask users to paste it into chat.

## Reference(s):

- [Pixmind skill page](https://clawhub.ai/fuyunzhishang/skills/pixmind-image)
- [Pixmind publisher profile](https://clawhub.ai/user/fuyunzhishang)
- [Pixmind image model routing](references/model-routing.md)
- [Pixmind model catalog endpoint](https://aihub-admin.aimix.pro/api-platform/v1/models)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown text with generated image attachments or JSON task results from Pixmind tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model name, task ID, output count, and generated image attachments after successful polling.]

## Skill Version(s):

2.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

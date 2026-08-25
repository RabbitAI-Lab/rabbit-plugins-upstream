## Description:

AI-HIVE skill for generating and editing Seedream 5.0 Lite images from text prompts and optional reference images, with task submission, status polling, and result download support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, designers, marketing teams, and brand teams use this skill to create or edit product, advertising, poster, and social-media images through AI-HIVE with optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad implicit invocation could route unrelated prompts or files to a third-party, potentially billable AI-HIVE service.

Mitigation: Require user confirmation before uploading reference files, starting batches, or using the skill for broad automatic routing.

Risk: API keys are required for AI-HIVE account access.

Mitigation: Store keys only in the configured local file or environment variables, review the stored key location, and avoid sharing keys in prompts, screenshots, or repositories.

Risk: Generated commercial images can contain inaccurate text, product claims, brand elements, or unauthorized likeness or style references.

Mitigation: Confirm source product facts and usage rights for reference materials, then manually review generated images before publication.

## Reference(s):

- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-model-expert-seedream-5-lite)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with shell command examples and downloaded image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload reference images to AI-HIVE, submit billable generation tasks, save task IDs, poll status, and download generated image files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

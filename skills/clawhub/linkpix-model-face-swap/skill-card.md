## Description:

Guides an agent through LinkPix/qhkit workflows for replacing or localizing the model in e-commerce product images and videos while keeping clothing, pose, composition, and lighting consistent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce teams use this skill to replace or localize models in product images and videos for cross-border e-commerce presentation. Agents use it to guide qhkit setup, prepare image or video replacement commands, confirm paid generation parameters, and return generated media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided images or videos are uploaded to the third-party LinkPix/qinghu service for generation.

Mitigation: Use the skill only with media approved for third-party processing and avoid submitting sensitive or unauthorized content.

Risk: Face-swap workflows can be misused with a person's likeness without authorization.

Mitigation: Confirm the user has rights to use the likeness and refuse unauthorized face replacement requests.

Risk: The skill requires a qhkit API key or token for service access.

Mitigation: Store credentials through qhkit configuration or environment variables and do not expose tokens in prompts, logs, or shared outputs.

Risk: Generated edits may change product details, text, logos, or model appearance.

Mitigation: Review generated outputs before commercial use, especially key product structure, branding, and visual claims.

Risk: Generation may consume service credits.

Mitigation: Run estimates when available and confirm model, inputs, duration, image count, size, and expected cost before submitting generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-model-face-swap)
- [@iqinghu/qhkit npm Package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit image or video generation jobs through qhkit after user approval; generated media URLs are returned by the service.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

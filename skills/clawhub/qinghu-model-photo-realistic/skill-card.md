## Description:

This skill helps agents retouch model and person photos with Qinghu AI by reducing AI-like artifacts, improving skin tone and texture, repairing details, and upscaling output for ecommerce imagery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to process ecommerce model or portrait images that look artificial, over-smoothed, or plasticky. It guides image submission, cost estimation, confirmation, polling, and delivery for one image at a time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected model or person images are sent to Qinghu's service.

Mitigation: Install and use the skill only when that data transfer is acceptable for the image and use case.

Risk: The skill requires a Qinghu API key.

Mitigation: Keep the key private and configure it only through the documented qhkit configuration or environment variable path.

Risk: Image generation is a paid workflow that can spend credits.

Mitigation: Run cost estimation first and require user confirmation of the quoted credit cost before generation.

Risk: The workflow is intended for model and person photos, not generic product, scenery, or non-person image edits.

Mitigation: Use the skill only for model or portrait photos and route other image types to a more appropriate image-editing skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-model-photo-realistic)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides one model/person image submission at a time and returns generated image URLs after polling completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

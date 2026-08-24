## Description:

Creative Scene helps agents generate or edit ecommerce-style images with dLazy banana-pro from text prompts or reference images, including reusable prompt templates for model, pose, and outfit changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and developers use this skill to draft product and lifestyle images from natural-language scene descriptions or to edit reference images by changing model attributes, poses, or outfits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external dLazy CLI package and hosted dLazy API for image generation.

Mitigation: Review the @dlazy/cli package and dLazy service terms before installing or running the skill.

Risk: Prompts, parameters, and any supplied reference image paths are sent to dLazy services, and referenced media may be uploaded for inference.

Mitigation: Only use prompts and images that are appropriate to send to the hosted service.

Risk: The dLazy API key is a paid-service credential that may be stored locally or supplied through DLAZY_API_KEY.

Mitigation: Protect the key like other service credentials and rotate or revoke it from dLazy if needed.

Risk: The artifact states that the skill should not be used to generate specific real-person portraits, inappropriate minor content, or fake product evidence.

Mitigation: Review prompts and outputs for those prohibited uses before using generated images in commercial workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/creative-scene)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy ecommerce detect-task skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses; generated images may be saved as files or returned as URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy banana-pro through the dLazy CLI; optional reference images are uploaded to dLazy and generated assets are hosted on files.dlazy.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates batches of ecommerce video advertising assets with LinkPix/qhkit from product information, reference images, model choices, and placement settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, ecommerce operators, and agents supporting external users use this skill to prepare multiple LinkPix video ad variants for paid media, brand promotion, and social media campaigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected product images, videos, prompts, and an API key to the LinkPix/Qinghu service through qhkit.

Mitigation: Use it only when the user is comfortable with that service path and credential requirement.

Risk: Video generation can consume paid credits and submitted tasks cannot be cancelled.

Mitigation: Before generation, show the model, count, format, references, and estimated credits, then wait for explicit user approval.

Risk: Incorrect or unavailable model labels can cause failed or unintended generation requests.

Mitigation: Fetch current qhkit options before choosing a model and use labels exactly as returned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-ad-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu account portal](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with qhkit command examples and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides the agent through model selection, credit estimation, user approval, task polling, and delivery of generated video URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

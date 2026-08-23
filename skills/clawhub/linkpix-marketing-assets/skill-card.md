## Description:

Generates ecommerce marketing assets with LinkPix/qhkit, including product images, scene images, detail pages, promotional posters, ad images, and ad videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and developers use this skill to plan, price, generate, and deliver image and video marketing asset packages for online sales channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload referenced product images to the LinkPix/qhkit provider.

Mitigation: Use only authorized product images and avoid confidential assets unless the user has approved that provider workflow.

Risk: Generation can consume paid credits after task submission.

Mitigation: Run an estimate when supported and obtain explicit user confirmation of model, count, duration, quality, reference images, and expected credits before generate actions.

Risk: The qhkit API token may be stored locally or exposed if pasted into chat.

Mitigation: Prefer local environment variables or qhkit config commands for secrets, and avoid echoing tokens back to the user.

Risk: The skill may install or update the qhkit CLI tooling.

Mitigation: Install the declared npm package only when the user intends to use the provider, and surface installation or network errors clearly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON results with generated image or video URLs, task IDs, and credit usage.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

LinkPix helps agents plan and generate ecommerce marketing assets, including product images, scene images, detail-page visuals, promotional posters, ad images, and ad videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and marketing teams use this skill to turn product promotion needs into a checklist of image and video assets and generate them through the qhkit CLI. It is suited for bundled marketing deliverables such as main product images, detail-page assets, promotional posters, ad creatives, and short ad videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install qhkit globally and requires a qhkit API token.

Mitigation: Use the documented qhkit setup flow, keep tokens scoped to the provider account, and avoid exposing credentials in shared logs or prompts.

Risk: The skill uploads selected media files to the provider for image or video generation.

Mitigation: Provide only files needed for the requested marketing asset and avoid unrelated private, confidential, or sensitive media.

Risk: Generation can spend service credits.

Mitigation: Run an estimate first and submit generation only after the user confirms the key parameters and expected credit cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with qhkit JSON command examples and generated media delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the qhkit CLI and a qhkit API token; paid generation is gated by estimate and explicit user confirmation.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

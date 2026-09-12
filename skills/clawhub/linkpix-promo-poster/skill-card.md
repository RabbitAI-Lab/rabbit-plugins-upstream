## Description:

Generates ecommerce promotion posters and campaign images for launches, discounts, seasonal sales, and brand marketing through the LinkPix/qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketing teams, and ecommerce operators use this skill to ask an agent for product promotion posters, discount campaign images, seasonal sale visuals, and launch materials. The skill guides the agent to prepare qhkit image-generation requests, optionally using a local product image as visual reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to install or upgrade qhkit globally from npm, including unpinned latest-version upgrades.

Mitigation: Require explicit user approval before installs or upgrades, prefer pinned package versions in controlled environments, and avoid global mutation on sensitive systems.

Risk: The workflow can upload referenced local product images to the LinkPix/qhkit service.

Mitigation: Confirm the user is comfortable uploading the specific image files before generation and avoid sending confidential or regulated product assets without authorization.

Risk: The workflow requires handling a LinkPix API token or QHKIT_TOKEN.

Mitigation: Use environment variables or the qhkit config mechanism without exposing token values in chat, logs, generated files, or screenshots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-promo-poster)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image-generation URLs from the qhkit service and should report returned credit usage when generation completes.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

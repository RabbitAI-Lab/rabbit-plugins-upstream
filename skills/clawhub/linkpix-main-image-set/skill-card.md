## Description:

Generates platform-styled ecommerce main images and carousel sets from a product image using LinkPix's qhkit service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce sellers and creative teams use this skill to turn a product image into platform-specific main images and carousel sets without writing image-generation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images provided to the skill are uploaded to the qhkit/iqinghu service.

Mitigation: Use only product images and copy that you are comfortable sending to that service.

Risk: Setup may install Node and qhkit and requires a qhkit API token.

Mitigation: Review installation steps and use a reviewed or pinned qhkit version where strict supply-chain controls apply; handle the API token securely.

## Reference(s):

- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with generated image URLs and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful results include links to generated images and the actual credits charged.]

## Skill Version(s):

0.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

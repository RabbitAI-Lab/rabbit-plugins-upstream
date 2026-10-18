## Description:

Helps agents generate white-background product images from individual or batched source photos using LinkPix.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and content teams use this skill to turn product photos into consistent white-background listing images, including batches of photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update qhkit, download a Node runtime, and change the local environment.

Mitigation: Use a managed or sandboxed environment with a pinned qhkit version, and approve installation or environment changes before execution.

Risk: Product photos are uploaded to a third-party service and the workflow may configure a service token.

Mitigation: Approve uploads and credential setup explicitly; share only images and credentials appropriate for that service.

Risk: Generative redraw can alter product text, logos, or structural details.

Mitigation: Review each generated image against its source before publishing a listing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/linkpix-white-background)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [White-background JPG or PNG image URLs with text guidance and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generative redraw may change product details; output does not include a transparent alpha channel.]

## Skill Version(s):

0.1.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

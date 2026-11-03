## Description:

Image matting tool: separates foreground from background and returns a transparent-background image URL for product image processing, character cutouts, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and image editors can remove backgrounds from product or character images and use the returned transparent image URL in compositing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images supplied for processing are uploaded to dLazy's hosted service, and generated images are hosted there.

Mitigation: Submit only images you are authorized to send to the service, and avoid sensitive images unless cloud processing is appropriate.

Risk: Use requires a dLazy API key and spends service credits; the key is saved in the local CLI configuration when using the recommended login flow.

Mitigation: Protect the local configuration, check the cost estimate with --dry-run when useful, and rotate or revoke the key when it is no longer needed.

Risk: The external CLI build, credential-permission enforcement, and hosted service behavior have not been verified.

Mitigation: Review the CLI source and service terms before installing or sending images.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-imageseg)

## Skill Output:

**Output Type(s):** [Image, JSON, URL]

**Output Format:** [JSON response containing a hosted transparent-image URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image is hosted by dLazy; asynchronous requests may initially return a task ID.]

## Skill Version(s):

1.3.37 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

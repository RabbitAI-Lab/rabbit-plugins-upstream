## Description:

Generates multiple marketing-ready product image variations from one source image, with support for different backgrounds, layouts, and design styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, marketers, and creative teams use this skill to direct an agent through qhkit-based generation of product-ad image variants for A/B testing, campaign rotation, and batch creative production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on running a third-party qhkit npm package that may execute with the user's account permissions.

Mitigation: Install only a pinned, reviewed qhkit version in an isolated environment when possible, and avoid blindly executing upgrade commands emitted by the CLI.

Risk: Image inputs and QHKIT_TOKEN values may be exposed beyond the local agent environment during generation.

Mitigation: Provide only the image files and token values needed for the current job, and avoid uploading unnecessary or sensitive assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-image-variations)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline bash commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command outputs such as generated image URLs and credit usage when the agent executes the workflow.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

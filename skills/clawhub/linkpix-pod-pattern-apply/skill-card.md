## Description:

Applies uploaded print patterns to apparel, hats, mugs, and other product images with perspective, lighting, and wrinkle-aware mockup generation through the qhkit image workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce teams, POD sellers, and agents use this skill to create realistic product mockups by applying a supplied pattern image to a target product or to a text-specified product carrier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on installing and running the qhkit npm CLI, including upgrade paths that may use mutable package versions.

Mitigation: Review and pin the qhkit package version before deployment; avoid unversioned npx and @latest in controlled environments.

Risk: The workflow may upload selected local product and pattern images to the provider.

Mitigation: Use only approved images, work from a restricted directory, and avoid uploading sensitive or unlicensed assets.

Risk: The qhkit token can grant provider access if exposed in shell history, logs, or shared workspaces.

Mitigation: Use a revocable token with limited exposure and prefer environment or secret-management practices appropriate for the runtime.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-apply)
- [Publisher profile: autoagc](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs and credit usage details when the qhkit image workflow is executed.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Generates LinkPix storyboard plans with shot design, camera-movement suggestions, copy scripts, and storyboard images for video production.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to turn product or campaign inputs into a storyboard script and generated storyboard images through LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit, Node, or global npm packages.

Mitigation: Preinstall qhkit through a controlled process and require user confirmation before any install or upgrade.

Risk: The skill may upload local reference images and submit paid LinkPix/qhkit tasks.

Mitigation: Confirm the selected files, task parameters, and estimated credits with the user before submission.

Risk: The skill may reuse an existing LinkPix/qhkit token from the local environment.

Mitigation: Run it only in environments where that credential reuse is intended and acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with inline shell commands and generated storyboard media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated storyboard image links and credit-usage details after user-confirmed paid task submission.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

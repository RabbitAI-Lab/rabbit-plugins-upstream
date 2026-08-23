## Description:

Generates video storyboard plans with shot design, camera-movement guidance, script copy, and storyboard images through the LinkPix/qhkit workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent users use this skill to turn product images and selling points into a storyboard script and optional storyboard images for video planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade Node/npm tooling to run qhkit.

Mitigation: Preinstall and review qhkit in a managed environment before enabling the skill, or require explicit approval before any package installation.

Risk: Product images are processed locally and may be uploaded to LinkPix/qhkit services.

Mitigation: Use only images intended for external processing and review file paths or URLs before submitting generation tasks.

Risk: The workflow may ask for or configure an iqinghu API key.

Mitigation: Provide credentials through a secure secret-management path instead of chat when possible, and avoid storing reusable API keys in conversation logs.

Risk: Storyboard script and image generation can consume service credits.

Mitigation: Run estimate actions where supported and require user confirmation of parameters and expected credit cost before submitting paid tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-storyboard)
- [autoagc Publisher Profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iqinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Images]

**Output Format:** [Markdown guidance with qhkit command examples, storyboard script text, JSON command responses, and generated storyboard image deliverables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local image paths or URLs as inputs, submits paid qhkit tasks after user confirmation, and may require polling for generated storyboard images.]

## Skill Version(s):

0.1.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

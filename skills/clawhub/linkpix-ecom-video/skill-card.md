## Description:

Routes ecommerce video generation requests to LinkPix qhkit commands for scripts, storyboards, text/image-to-video generation, and multi-image quick video creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn ecommerce product, advertising, and promotional video requests into the appropriate LinkPix qhkit workflow. It helps select models or templates, estimate credits where supported, confirm cost-impacting parameters, submit generation tasks, poll status, and return video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may prompt agents to perform persistent global npm or Node installations and qhkit upgrades.

Mitigation: Preinstall qhkit from a trusted source where possible and require explicit user approval before installing or upgrading tooling.

Risk: The skill can reuse a local Qinghu/OpenClaw token or configure a token for qhkit.

Mitigation: Confirm token use with the user, keep credentials out of shared logs, and prefer environment or local configuration mechanisms that avoid exposing raw secrets.

Risk: Referenced local media files may be uploaded to the LinkPix/qhkit service during generation.

Mitigation: Confirm which media files will be used before generation and avoid submitting confidential or unauthorized assets.

Risk: Generate commands can consume credits and tasks cannot be canceled after submission.

Mitigation: Run estimates when supported and require explicit approval of model, duration, orientation, media inputs, and expected credit use before submitting generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON command examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit install or upgrade steps, token configuration guidance, media upload paths, credit estimates, task IDs, status polling instructions, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps agents upscale and repair video clarity with LinkPix/qhkit, including 1080p, 2K, and 4K targets at 30 or 60 fps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent prepare LinkPix/qhkit video super-resolution work, confirm resolution and frame-rate settings, submit jobs after user approval, poll for completion, and return resulting video URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video inputs may be uploaded to the LinkPix/iQingHu service through qhkit.

Mitigation: Avoid using sensitive videos unless the user trusts the provider and understands the upload path.

Risk: Submitting a generation job can spend account credits.

Mitigation: Estimate credits when supported and obtain explicit user confirmation before running generate actions.

Risk: Broad video-quality trigger wording may activate the skill for loosely related requests.

Mitigation: Confirm that the user wants LinkPix/qhkit video super-resolution before submitting any paid or upload-producing action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-video-upscale)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [iQingHu account portal](https://www.iqinghu.com)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, credit estimates, status messages, and generated video URLs.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

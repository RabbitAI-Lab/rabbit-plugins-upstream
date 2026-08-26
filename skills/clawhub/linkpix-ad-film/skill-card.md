## Description:

Guides an agent through LinkPix/qhkit setup, prompt refinement, credit estimation, approved submission, status polling, and delivery for cinematic product advertising videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and developers use this skill to create high-production product advertising videos with LinkPix/qhkit. The skill helps collect required media, choose live model labels, estimate credit cost, obtain approval before generation, poll task status, and return the finished video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may upload user-provided images or audio to the LinkPix/Qinghu provider.

Mitigation: Use a dedicated API key where possible and avoid providing sensitive media that should not be sent to the provider.

Risk: Generation can spend account credits after a job is submitted.

Mitigation: Repeat the selected model, media, duration, and estimated credit cost, then wait for explicit user approval before running generation.

Risk: The skill installs or invokes the qhkit CLI and may install Node when it is missing.

Mitigation: Prefer the declared npm package, verify downloaded Node checksums when bootstrapping, and surface installation or network failures to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, credit estimates, status updates, generated video URLs, and user-facing error messages.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

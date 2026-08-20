## Description:

This skill helps agents generate cinematic product advertising videos with LinkPix through the qhkit CLI, including credit estimates, job submission, status polling, and video URL delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create product advertising or brand-promotion videos from reference images and precise scene prompts. It is suited for workflows that need cost estimation, asynchronous video generation, status tracking, and delivery of generated media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit or Node in the execution environment.

Mitigation: Prefer a preinstalled, pinned qhkit in a user-scoped environment, and require explicit approval before any global install, Node installation, or upgrade.

Risk: The skill uploads product images or videos to the Qinghu/LinkPix service and may spend API credits.

Mitigation: Confirm that the user approves the upload and cost before generation; use qhkit estimate when available and report credit usage.

Risk: The skill can reuse existing OpenClaw credentials automatically.

Mitigation: Confirm credential source and user intent before reusing local credentials, especially in shared or production environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, credit estimates, status messages, generated video URLs, and user-facing failure messages from qhkit.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

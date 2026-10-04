## Description:

Helps brand, creator, and ad teams generate YouTube-oriented product marketing videos with qhkit/LinkPix workflows for model selection, asset upload, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External brand marketers, creators, advertising teams, and agent operators use this skill to plan and run YouTube product videos, YouTube Ads assets, brand-channel videos, affiliate marketing videos, and related video-generation jobs through qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install or update npm and Python tooling and configure qhkit locally.

Mitigation: Install only after user confirmation, review the exact package source and command, and prefer the least-privileged installation path that works.

Risk: The qhkit workflow can require API tokens or other credentials.

Mitigation: Prefer a secure secret store or environment variable, avoid pasting raw keys into chat, and redact credentials from logs and command output.

Risk: Video generation jobs may consume credits and cannot be cancelled after submission.

Mitigation: Confirm model, duration, orientation, language, reference assets, and estimated credits with the user before running generation commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-youtube-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, model options, credit estimates, status results, and generated video URLs when the agent executes the workflow.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

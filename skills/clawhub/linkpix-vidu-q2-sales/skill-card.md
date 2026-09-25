## Description:

Helps ecommerce merchants, designers, and independent-store operators use QHKit to create Vidu Q2 product marketing videos from product images and selling points, including task submission, polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and content creators use this skill to prepare and submit QHKit Vidu Q2 video-generation jobs for product showcases, storefront media, and advertising creatives. It guides model selection, parameter confirmation, credit estimation, task polling, and final video delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to install or upgrade Node/npm tooling and the qhkit CLI.

Mitigation: Use a controlled environment with Node and qhkit preinstalled where possible, and review any global install, upgrade, or PATH change before execution.

Risk: The skill processes local product images for upload to QHKit.

Mitigation: Use only product images approved for external processing and avoid submitting sensitive or regulated media unless the service is approved for that data.

Risk: QHKit API keys are required for authenticated use.

Mitigation: Treat the QHKit token as a sensitive credential, prefer environment variables or the supported config flow, and avoid exposing the token in chat or logs.

Risk: Video generation can consume credits and submitted tasks may not be cancelable.

Mitigation: Run estimates when supported and require explicit user confirmation of model, duration, inputs, orientation, language, and expected credits before submitting a generation job.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q2-sales)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [QHKit API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return QHKit task IDs, status summaries, credit estimates, and generated video URLs.]

## Skill Version(s):

0.1.2 (source: server release metadata, released 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

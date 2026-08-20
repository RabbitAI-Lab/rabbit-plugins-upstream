## Description:

青虎AI 双人爆款视频模仿 helps an agent submit and monitor a Qinghu two-person video imitation workflow that uses a two-person reference video and optional character image to generate synchronized duo marketing or creator videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare parameters, estimate cost, submit, poll, and deliver results for Qinghu AI two-person video imitation workflows. It is intended for scenes with two visible people, such as duo product videos, parent-child clips, partner appearances, or synchronized action imitation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs global Node/qhkit installation and software bootstrapping.

Mitigation: Prefer a managed qhkit and Node installation, review install commands before execution, and avoid automatic system-wide bootstrapping when a controlled runtime is available.

Risk: The skill requires Qinghu credentials and may persist API-token configuration.

Mitigation: Use scoped or environment-provided Qinghu credentials where possible and avoid storing broad or long-lived tokens on shared systems.

Risk: Generation requests can consume paid Qinghu credits.

Mitigation: Run the estimate step with the exact generation parameters and get user confirmation of the quoted credit cost before submitting a workflow.

Risk: Using unlicensed reference videos or people images, especially minors, can create rights and consent issues.

Mitigation: Use only self-owned or authorized media and confirm appropriate consent before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Markdown]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-facing status, cost, delivery, and error guidance for qhkit workflow commands; final media URLs are returned by the external Qinghu workflow status response.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

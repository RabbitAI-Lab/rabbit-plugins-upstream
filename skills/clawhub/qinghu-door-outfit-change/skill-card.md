## Description:

Guides an agent through Qinghu AI's door-opening outfit-change workflow to generate a short video from one model image, up to four clothing images, and optional audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agent operators use this skill to prepare, price, submit, and monitor Qinghu AI outfit-change video jobs for authorized model and clothing assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads model, clothing, and optional audio assets to the Qinghu qhkit service.

Mitigation: Use only assets the user owns or is authorized to process, and avoid sensitive personal media unless the user has accepted the upload risk.

Risk: Generating a video can spend Qinghu credits after submission.

Mitigation: Run an estimate first, report expected credits, and require explicit user confirmation before calling generate.

Risk: The skill handles paid-service API credentials and may install or upgrade command-line dependencies.

Mitigation: Prefer a platform-managed or temporary token, review dependency installation before use, and avoid sharing long-lived credentials with the agent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit JSON responses, generated media URLs, log IDs, and credit-use reporting.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

青虎AI 达人数据引擎 accepts Douyin, Xiaohongshu, and Bilibili creator profile links, submits a Qinghu workflow, and returns standardized Excel exports with account basics and core playback metrics for creator and competitor monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to batch collect creator account metrics from Douyin, Xiaohongshu, and Bilibili profile links. It supports daily monitoring of partner creators, competitor accounts, follower changes, playback metrics, and Excel data exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime installation can broaden the execution environment, including package installs or Node bootstrap steps.

Mitigation: Prefer a preinstalled qhkit binary or a controlled package installation path before running workflow commands.

Risk: Persistent Qinghu API credentials may be exposed if passed directly in command arguments or unmanaged files.

Mitigation: Provide credentials through a secret manager, environment variable, or controlled qhkit configuration file.

Risk: Generate calls can consume paid Qinghu credits.

Mitigation: Run the estimate command first and confirm the reported credits before submitting a generate request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command blocks; the invoked workflow returns JSON status and downloadable Excel files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow supports up to 5 creator homepage links per run and requires a qhkit token or configured qhkit environment.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

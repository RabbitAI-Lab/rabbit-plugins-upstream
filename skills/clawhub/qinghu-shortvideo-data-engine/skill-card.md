## Description:

Batch exports playback, like, share, favorite, and comment metrics for Douyin, Xiaohongshu, and Bilibili video links into an Excel report for short-video performance monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to collect metrics for their own or competitor short videos, estimate paid Qinghu credit usage, submit a Qinghu workflow, and retrieve the resulting Excel file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend paid Qinghu credits when submitted.

Mitigation: Run the estimate action first, present the exact parameters and estimated credits, and submit only after explicit user approval.

Risk: The workflow sends the provided video URLs to Qinghu and requires qhkit configuration with a Qinghu token.

Mitigation: Confirm the user is comfortable installing qhkit or Node if needed, configuring the token, and sharing only authorized video URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-shortvideo-data-engine)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON parameters; workflow completion returns an Excel .xlsx file URL.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit, a Qinghu API token, full-length supported platform video URLs, and explicit user approval before paid submission.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

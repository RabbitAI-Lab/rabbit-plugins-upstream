## Description:

This skill helps agents use Qinghu AI's qhkit workflow to collect creator profile metrics from Douyin, Xiaohongshu, and Bilibili profile links, estimate paid job cost, submit confirmed jobs, and return standardized Excel exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, social commerce, and creator operations teams use this skill to monitor competitor or partner creator accounts and export daily follower and playback metrics. It is intended for single-run Qinghu workflow submissions of up to five creator profile links, with recurring schedules configured in the Qinghu workbench.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow handles creator profile links and requires a Qinghu API key.

Mitigation: Confirm the user trusts Qinghu and qhkit with those inputs before installation or configuration, and avoid exposing the API key in shared logs or messages.

Risk: Submitting a generate job consumes Qinghu credits and cannot be treated as a read-only action.

Mitigation: Run estimate first, present the expected credit cost and key parameters to the user, and submit only after explicit approval.

Risk: The skill depends on the current online Qinghu workflow field labels and supports only creator profile links for Douyin, Xiaohongshu, and Bilibili.

Mitigation: Use the options action when fields are uncertain, copy returned labels exactly, and reject unsupported video links or batches above five profiles.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-creator-data-engine)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON parameter examples; completed jobs return XLSX file links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses qhkit workflow actions for options, estimate, generate, and status; generate requires explicit user approval because it consumes Qinghu credits.]

## Skill Version(s):

0.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

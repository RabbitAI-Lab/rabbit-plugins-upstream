## Description:

This skill helps agents use Qinghu AI's kidswear viral video imitation workflow to transfer actions from a reference video onto a child model image for short product videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, commerce teams, and agents use this skill to prepare, estimate, submit, and monitor a Qinghu AI workflow that adapts a reference video to an authorized child model image for kidswear product videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads child-model images and reference videos to Qinghu, including during local-media estimation.

Mitigation: Use only self-owned or authorized media, confirm guardian consent for child images, and tell the user before any estimate or generation step that uploads may occur.

Risk: Paid generation consumes Qinghu credits and submitted tasks may not be cancelable.

Mitigation: Run an estimate with the exact parameters, disclose expected credits and key inputs, and wait for explicit user approval before running generate.

Risk: Online workflow fields, pricing, and available options can change after the documented snapshot.

Mitigation: Use qhkit workflow options and estimate as the current source of truth instead of relying on the embedded field or pricing snapshot.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs and a final Qinghu credit-consumption line after successful paid generation.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

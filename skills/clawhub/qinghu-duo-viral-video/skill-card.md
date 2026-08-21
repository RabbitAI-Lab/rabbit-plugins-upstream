## Description:

Guides an agent through Qinghu AI's two-person viral video imitation workflow, using a reference video and optional person image to synchronize two visible subjects' movement and expressions for commercial video creation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to prepare, estimate, submit, monitor, and deliver Qinghu AI two-person video imitation jobs for short-form commerce, parent-child, partner, or duo scenes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected image and video media to Qinghu AI.

Mitigation: Confirm the user is comfortable sharing the selected media before submission and avoid private, third-party, commercial, or minor-related footage without the necessary rights and consent.

Risk: Generating a workflow consumes Qinghu credits and submitted jobs may not be cancellable.

Mitigation: Run an estimate first, present the exact parameters and expected credit use, and wait for explicit user confirmation before calling generate.

Risk: The workflow depends on the qhkit CLI and a Qinghu API token.

Mitigation: Confirm qhkit installation, version compatibility, and token configuration before attempting paid generation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-duo-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, JSON]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON workflow parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs and a final Qinghu credit-consumption line after workflow completion.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

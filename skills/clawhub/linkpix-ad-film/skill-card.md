## Description:

Generates cinematic LinkPix product advertising videos and brand TVC-style promotional clips through qhkit video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to plan, estimate, submit, monitor, and deliver high-end product advertising videos or brand promotional clips with LinkPix/qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to install or upgrade qhkit, executing changing third-party code.

Mitigation: Review and approve package installs or upgrades before execution, and avoid running upgrade commands copied directly from CLI response messages.

Risk: Local media paths supplied to qhkit may be uploaded to the provider.

Mitigation: Use only media intended for upload and avoid supplying confidential, private, or unlicensed files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, status updates, credit estimates or charges, and resulting video URLs returned by qhkit.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

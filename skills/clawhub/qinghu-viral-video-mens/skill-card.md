## Description:

This skill guides an agent through Qinghu AI's menswear viral-video imitation workflow, using qhkit to upload a reference video and model image, estimate credits, submit the paid action-transfer job, poll status, and return generated video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to create menswear short-form product videos by transferring motion from an authorized reference video to a supplied model image through Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads reference videos and model images to Qinghu AI, which can expose private, sensitive, or licensed media.

Mitigation: Use only materials the user owns or is licensed to process, avoid sensitive media, and confirm upload is acceptable before using qhkit.

Risk: The generate action creates a paid Qinghu task and can consume credits.

Mitigation: Run an estimate with the exact parameters, show the expected charge and selected media, and wait for explicit user approval before submitting.

Risk: Action-transfer outputs can misuse another person's likeness or copyrighted footage.

Mitigation: Confirm rights and consent for the source video, model image, and intended commercial distribution before producing or sharing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-mens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated video URLs after qhkit status reports completion.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

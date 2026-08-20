## Description:

This skill helps agents use Qinghu AI to create child-clothing promotional videos by transferring motion from a reference video to an authorized child model image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and commerce teams use this skill to prepare Qinghu workflow commands for child-clothing short-form videos from a reference video and model image. It guides setup, estimate confirmation, job submission, polling, and delivery of generated media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses child model images and reference videos, creating privacy, consent, and likeness concerns.

Mitigation: Confirm rights to the reference video and model image, and obtain guardian authorization for any minor's likeness before use.

Risk: The workflow installs and runs the third-party qhkit tool and may spend Qinghu credits.

Mitigation: Confirm the user intends to use Qinghu's service, review the estimate, and get user approval before generation.

Risk: Commercial reuse of copied or unauthorized reference videos may create rights issues.

Mitigation: Use only self-owned or properly licensed material for reference videos and generated promotional content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-viral-video-kids)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces qhkit workflow commands, setup guidance, estimate and polling steps, and final media delivery guidance.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

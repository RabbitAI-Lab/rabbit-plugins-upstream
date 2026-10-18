## Description:

Guides agents in using dLazy video segmentation to obtain a black-and-white human mask video for compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and developers use this skill to request a human-segmentation mask for a video and incorporate the result into compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media supplied to the CLI is uploaded to dLazy-hosted services.

Mitigation: Only submit media that you are willing to upload; review the linked CLI package before installation.

Risk: The skill's --prompt example conflicts with the documented --video option, which could cause failed invocations.

Mitigation: Check dlazy videoseg -h and use its documented video option before running a task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source link (skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a hosted mask-video result or an asynchronous task identifier; --save downloads the result.]

## Skill Version(s):

1.3.31 (source: ClawHub release metadata; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

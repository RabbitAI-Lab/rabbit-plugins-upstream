## Description:

Extracts the first frame and audio from a source video, analyzes it to create a prompt, and returns a Seedance 2.0 replication bundle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and video editors use this skill to analyze a reference video and prepare a Seedance 2.0 replication bundle containing a prompt, first frame, and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media are sent to dLazy services for processing.

Mitigation: Review dLazy service terms and avoid submitting confidential or sensitive media and prompts.

Risk: The security assessment was partial and noted a possible mismatch between the described workflow and authentication commands.

Mitigation: Check the installed CLI's current help and authentication behavior before using it with important work.

## Reference(s):

- [dLazy CLI project information](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON result with generated media URLs and optional asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated results may include a first frame, audio, and video; asynchronous runs can return a task ID before outputs are ready.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

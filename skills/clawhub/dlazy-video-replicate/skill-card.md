## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle (first frame + audio + video).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use the skill to analyze a source video and request a Seedance 2.0 replication bundle. It returns a structured result with links to generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial security review reports authentication commands that do not match the stated video-replication purpose, and some referenced details could not be resolved.

Mitigation: Review the CLI and its login/authentication behavior before use, and assess whether the service’s stated handling of prompts and uploaded media fits your needs.

## Reference(s):

- [dLazy CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Media assets]

**Output Format:** [JSON result with generated media URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous jobs may return a task identifier and status before media outputs are ready.]

## Skill Version(s):

1.3.39 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

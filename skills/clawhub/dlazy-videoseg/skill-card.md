## Description:

Creates a black-and-white human-segmentation mask video from a supplied video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video creators can use the generated mask video to isolate people for downstream compositing or matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment says the visible CLI commands do not establish that the external CLI performs the described video-segmentation task, and the CLI behavior was not established.

Mitigation: Before installing, check that the pinned CLI package and its documented behavior match the video-segmentation task; review its media data handling before use.

## Reference(s):

- [dLazy CLI source repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files, JSON]

**Output Format:** [Black-and-white mask video asset with JSON task and result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The mask video is described as matching the input video's duration; asynchronous tasks may first return a task ID.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

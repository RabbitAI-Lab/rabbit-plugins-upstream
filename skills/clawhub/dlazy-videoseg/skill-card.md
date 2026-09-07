## Description:

Video human segmentation tool that invokes Aliyun SegmentVideoBody through the dLazy CLI/API and returns a same-length black/white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production users use this skill to segment people from videos and produce mask assets for compositing or matting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party npm CLI and hosted dLazy API.

Mitigation: Install only if you trust dLazy and the pinned @dlazy/cli package; prefer the npx pinned invocation in a non-privileged environment.

Risk: Selected local media files are uploaded to dLazy media storage for processing.

Mitigation: Provide only the media files needed for the job and avoid sending sensitive or unauthorized content.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through the environment.

Mitigation: Avoid running npm as administrator/root and rotate the dLazy API key if local machine or package supply-chain compromise is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs or an async generateId/status when --no-wait is used; --save can download the generated asset locally.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

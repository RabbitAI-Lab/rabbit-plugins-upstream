## Description:

Video human segmentation tool that invokes Aliyun's asynchronous SegmentVideoBody service through the dLazy CLI and returns a same-length black-and-white mask video for downstream compositing or matting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and media automation agents use this skill to generate human segmentation mask videos from source video inputs for compositing, matting, and downstream video processing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external dLazy CLI and hosted API, so video inputs may be uploaded to dLazy services for processing.

Mitigation: Only submit media that is appropriate to upload to dLazy and review the linked CLI source and package before installation.

Risk: The dLazy API key is a sensitive credential stored locally or supplied through an environment variable.

Mitigation: Protect the local CLI config and DLAZY_API_KEY value, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: Global npm installation can modify the user's environment and should not be run with unnecessary privileges.

Mitigation: Prefer the pinned npx invocation when possible and avoid running npm install commands with elevated privileges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs, asynchronous task identifiers, or a saved local output asset when --save is used.]

## Skill Version(s):

1.3.15 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

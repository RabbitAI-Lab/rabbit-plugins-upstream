## Description:

Helps an agent lip-sync a talking-person video to a new voice track, with an optional reference image to select a face in multi-person footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a person's mouth movements in video with replacement speech, optionally selecting a face when the video contains multiple people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media supplied to the skill is uploaded to the dLazy service.

Mitigation: Only submit video, audio, and face images you intend to share with dLazy.

Risk: The skill installs and executes an external CLI package.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before installing it in sensitive environments.

Risk: An API key may be stored in local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistent key storage is unsuitable.

Risk: Some examples and output descriptions in the skill documentation are inconsistent with video lip-sync usage.

Mitigation: Check the CLI help and confirm the media inputs and result before running a paid job.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service can return a hosted generated-media URL; the CLI can optionally save the result locally.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Video replicate tool: extracts the first frame and audio from the source video, runs video understanding for a prompt, and returns a Seedance 2.0 replicate bundle with first-frame image, audio, and video outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to replicate a source video's structure by generating a Seedance 2.0 bundle through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media paths passed to the skill may be uploaded to dLazy for processing, and generated files are hosted by dLazy.

Mitigation: Use the skill only with media that may be processed by the dLazy service, and review dLazy service terms before use.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation credentials or npx execution when less local persistence is desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-replicate)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Media URLs]

**Output Format:** [JSON command response containing generated asset URLs or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return empty outputs with task status when --no-wait is used; generated files are hosted by dLazy.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

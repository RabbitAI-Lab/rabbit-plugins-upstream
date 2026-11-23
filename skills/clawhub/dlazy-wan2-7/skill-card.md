## Description:

通义万相 2.7 视频模型，支持文生视频、首尾帧生视频及参考图或视频生视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from text prompts, reference images or videos, or first and last frames through the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was benign at medium confidence but partial, and it noted a possible mismatch involving the login command.

Mitigation: Review the CLI behavior before authenticating, and only provide prompts and media you intend to send to the hosted dLazy service.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI source repository (listed in the skill documentation)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [JSON response containing generated asset URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is hosted by dLazy; local media supplied as input is uploaded to its media service.]

## Skill Version(s):

1.3.42 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

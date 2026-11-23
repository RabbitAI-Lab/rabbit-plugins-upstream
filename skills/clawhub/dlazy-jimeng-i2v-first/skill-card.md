## Description:

Generates videos from a single first-frame image and a text prompt using Jimeng (即梦).

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can use a first-frame image and a prompt to request a short Jimeng video. The skill is intended for image-to-video generation through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the release benign with medium confidence from a partial scan and flags a mismatch between its video-generation description and the login or authentication commands it found.

Mitigation: Before installing, confirm that dLazy login and API-key setup are expected, review the documented data flow and service terms, and avoid sending sensitive prompts or local images unless approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [dLazy API key management](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [Generated video asset and JSON task/result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may complete asynchronously; result assets are returned by URL.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

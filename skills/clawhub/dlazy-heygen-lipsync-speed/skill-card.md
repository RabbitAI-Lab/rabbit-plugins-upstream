## Description:

HeyGen Lipsync Speed: Fast lip-sync model, ideal for scenarios requiring rapid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to synchronize a video's mouth movements with supplied audio, with options for captions, duration adjustment, background music, and speech enhancement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and could not resolve some CLI and installation references.

Mitigation: Review the linked CLI project and pinned @dlazy/cli package before installing.

Risk: The skill sends supplied prompts to dLazy services and uploads local media for processing; API credentials are stored in the user's local CLI configuration.

Mitigation: Submit only media approved for external processing, protect the API key, and rotate or revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Media files, JSON]

**Output Format:** [JSON result containing generated media URLs and task status; generated media can be saved to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier before the generated media is ready.]

## Skill Version(s):

1.3.43 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

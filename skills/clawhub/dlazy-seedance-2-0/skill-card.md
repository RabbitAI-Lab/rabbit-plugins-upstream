## Description:

The skill is described as generating Seedance 2.0 videos from prompts, with multimodal references and first/last-frame workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use the skill to request Seedance video generation from text prompts or image, video, and audio references through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found a mismatch between the advertised video-generation purpose and the behavior it reviewed, and marked analysis partial.

Mitigation: Review the release and verify its behavior in an isolated environment before use; the available scan does not resolve the mismatch or analysis gaps.

Risk: Prompts and local image, video, or audio references are sent to dLazy services, and the skill requires an API key.

Mitigation: Use only media you are authorized to share, avoid sending confidential content unless approved, and keep the API key private and revocable.

## Reference(s):

- [Published skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy service](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project listed in skill metadata (not verified as release provenance)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Media files, JSON, API Calls, Shell commands]

**Output Format:** [Generated video or media assets, with a JSON result containing hosted output URLs and task status when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation uses a prompt and optional media references; settings can include duration, resolution, aspect ratio, and audio generation.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

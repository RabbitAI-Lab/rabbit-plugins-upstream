## Description:

Generates videos with ByteDance Seedance 2.0 Fast from text prompts, with support for multimodal references and first or last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts, with optional image, video, or audio references, or specified first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy services, and local media files are uploaded for generation.

Mitigation: Submit only media and prompts you are comfortable sharing with the service.

Risk: Video generation can spend dLazy credits.

Mitigation: Use --dry-run to preview the request and estimated cost before generation.

Risk: Login stores an organization API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy website](https://dlazy.com)
- [CLI repository (listed in skill metadata; skill provenance unavailable)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video asset URL and JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports 480p or 720p output and 4–12 second durations; asynchronous mode can return a task identifier.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

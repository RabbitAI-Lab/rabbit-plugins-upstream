## Description:

Guides agents to generate a lip-synced video from video and audio inputs using the dLazy CLI and hosted sync-lipsync v3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to align a speaker's lip movements with supplied audio for dubbing, localization, and virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video or audio supplied to the CLI may be uploaded to dLazy for hosted processing.

Mitigation: Get approval before submitting sensitive media and review the service's handling of uploaded files.

Risk: Installing the CLI globally or using saved authentication persists software or an API key locally.

Mitigation: Review the @dlazy/cli package before installation; consider pinned npx usage and a per-invocation DLAZY_API_KEY instead.

Risk: The supplied command example and sample image output do not match the documented video input and output workflow.

Mitigation: Confirm supported options with dlazy sync-lipsync-3 -h and inspect the actual response before relying on examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown instructions and CLI examples; the CLI returns JSON with a generated media URL or asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and video/audio inputs; check CLI help because the supplied example and sample output conflict with the stated video workflow.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

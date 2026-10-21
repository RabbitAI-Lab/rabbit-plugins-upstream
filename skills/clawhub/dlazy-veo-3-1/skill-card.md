## Description:

Helps generate cinematic videos from text prompts or images using Google Veo 3.1 through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video or image-guided video generation, extend videos, and retrieve generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to the dLazy cloud service.

Mitigation: Confirm with the user before uploading local media and avoid sharing sensitive prompts or files.

Risk: The CLI can persist an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials if local key storage is undesirable.

Risk: Video generation may incur charges.

Mitigation: Confirm before billable calls and use the dry-run option to check the estimated cost.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Video URLs]

**Output Format:** [Text and JSON with generated media links or an asynchronous task ID]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can optionally save generated media to a local file.]

## Skill Version(s):

1.3.31 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

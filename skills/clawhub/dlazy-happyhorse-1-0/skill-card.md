## Description:

Helps agents generate or edit videos from text, a first frame, reference images, or existing video using Happy Horse 1.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video, first-frame-to-video, reference-to-video, and video-editing jobs through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's cloud service.

Mitigation: Only submit prompts and files you are comfortable uploading to dLazy.

Risk: The third-party CLI must be installed or run, and authentication uses an API key that can be stored locally.

Mitigation: Review the linked CLI source and package in sensitive environments, use the pinned npx command to avoid a persistent global install, and supply DLAZY_API_KEY per run if local key storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON containing generated media URLs or an asynchronous task ID.]

## Skill Version(s):

1.3.28 (source: ClawHub release metadata; skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

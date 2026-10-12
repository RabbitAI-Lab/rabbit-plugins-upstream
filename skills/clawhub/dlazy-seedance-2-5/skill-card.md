## Description:

Helps agents generate short videos from text prompts and optional image, video, audio, or first-and-last-frame references through dLazy's Seedance 2.5 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to request short AI-generated videos from prompts and optional media references, including control over duration, resolution, and aspect ratio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external dLazy CLI uses an API key that can be saved locally.

Mitigation: Review the CLI before installing, and use a per-invocation DLAZY_API_KEY instead of saving a key if persistence is undesirable.

Risk: Media supplied for generation is uploaded to the dLazy service.

Mitigation: Only pass images, videos, and audio that you intend to share with the service.

Risk: Generation requests may consume account credits.

Mitigation: Check the estimated cost before submitting a request.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository (linked in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and JSON result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service returns generated media URLs; asynchronous requests may return a task ID for later status checks.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

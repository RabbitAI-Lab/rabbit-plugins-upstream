## Description:

Guides agents in generating videos with Seedance 2.0 from text prompts, multimedia references, or first and last frames through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide video generation from prompts and optional images, videos, audio, or first and last frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be sent to the third-party dLazy service.

Mitigation: Review prompts and media before submission and avoid sharing sensitive content.

Risk: Logging in can save an API key in local CLI configuration.

Mitigation: Use DLAZY_API_KEY for session-based access when persistent credentials are undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and descriptions of JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return a hosted result URL or an asynchronous task ID; an optional flag saves the generated asset locally.]

## Skill Version(s):

1.3.22 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

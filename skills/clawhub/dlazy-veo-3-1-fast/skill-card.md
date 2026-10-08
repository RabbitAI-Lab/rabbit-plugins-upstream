## Description:

Guides agents in generating short videos from text or images with Google Veo 3.1 Fast through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide text-to-video, image-to-video, and video-extension requests through dLazy's Veo 3.1 Fast service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly supplied media may be sent to the hosted dLazy service.

Mitigation: Avoid supplying sensitive prompts or media without reviewing the service terms and your data-handling requirements.

Risk: Login can store an API key locally, and invoking the skill requires an external npm CLI.

Mitigation: Protect the local CLI configuration and review the upstream package before use; use the pinned npx invocation to avoid a global install.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and example JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return hosted media URLs or asynchronous task IDs; an optional save flag downloads a result.]

## Skill Version(s):

1.3.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

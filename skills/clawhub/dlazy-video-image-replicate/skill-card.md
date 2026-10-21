## Description:

Studies a supplied image or video reference and helps recreate its look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and other users can use a supplied image or video as a visual reference to remake its style and structure with their own content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files can be sent to dLazy's hosted service.

Mitigation: Confirm the task is a reference remake and avoid sending private files unless sharing them with dLazy is acceptable.

Risk: Authentication can save an API key locally.

Mitigation: Use a per-invocation API key environment variable if local key storage is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text streamed to the terminal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based follow-up conversations can retain context.]

## Skill Version(s):

1.3.32 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

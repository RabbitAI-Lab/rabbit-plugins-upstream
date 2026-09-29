## Description:

Helps agents create or edit videos from text, a starting frame, or reference images using Happy Horse 1.0.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide text-to-video, first-frame-to-video, reference-to-video, and video-editing requests through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication may store a dLazy API key locally.

Mitigation: Confirm trust in the dLazy CLI and service before installing or saving a key.

Risk: Generation may consume paid credits.

Mitigation: Check the cost estimate before submitting a paid request.

Risk: Prompts and explicitly supplied media may be uploaded to dLazy-hosted endpoints.

Mitigation: Share only prompts and files you are comfortable sending to the service.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report a hosted result URL or an asynchronous task ID.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Guides an agent to select and run dLazy commands for image, video, and audio generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to select a dLazy model and generate or transform images, videos, and audio through the hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger words may cause unintended use of the hosted service with saved credentials.

Mitigation: Confirm the user's intent before invoking dLazy, especially when credentials are already stored.

Risk: Prompts or local media supplied to the skill may be uploaded to dLazy.

Mitigation: Avoid sensitive prompts and private files unless the user accepts the upload.

Risk: A saved API key remains available to later CLI invocations.

Mitigation: Prefer a per-run DLAZY_API_KEY on shared machines; revoke or rotate saved keys when no longer needed.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown instructions and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI responses provide generated media URLs in JSON.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

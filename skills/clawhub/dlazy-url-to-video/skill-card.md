## Description:

Turns a webpage URL into a promo, social ad, or product demo video by capturing the page, deriving brand context, storyboarding, voiceover, and building the video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing teams use this skill when they have a URL or webpage and want an agent to start or continue a dLazy website-to-video project for a promo, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and project context are sent to dLazy's hosted API.

Mitigation: Use the skill only for URL or webpage-to-video tasks where sending that information to dLazy is acceptable.

Risk: Files attached with the CLI are uploaded to dLazy media storage before use.

Mitigation: Avoid attaching sensitive local files unless upload to dLazy is approved for the task.

Risk: Authentication stores or uses a dLazy API key.

Mitigation: Prefer scoped keys, rotate or revoke keys from the dLazy dashboard when needed, and use per-invocation environment variables when persistent local config is not desired.

Risk: Global npm installation persists a third-party CLI binary on the system.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global binary is not required.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI invocation for new website-to-video projects and project-scoped follow-up turns.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

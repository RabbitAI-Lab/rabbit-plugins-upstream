## Description:

Paste a URL and use dLazy's hosted website-to-video agent to turn the page into a promo, social ad, or product demo video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill when they have a webpage URL and want an agent to create a promo, social ad, or product demo video through dLazy's hosted URL-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends the provided URL, prompts, project context, and explicitly attached files to dLazy's hosted service.

Mitigation: Use the skill only for data you are comfortable sending to dLazy, and avoid attaching sensitive local files unless the user has approved that transfer.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication when persistence is not desired, and rotate or revoke the key if the machine is shared or exposure is suspected.

Risk: A global CLI install leaves a persistent binary on the system.

Mitigation: Prefer the pinned npx invocation when a temporary install path is more appropriate, or install the pinned global package only after reviewing the package source and terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell command examples and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes work through the pinned dLazy CLI and may reference project ids for multi-turn continuation.]

## Skill Version(s):

1.0.9 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

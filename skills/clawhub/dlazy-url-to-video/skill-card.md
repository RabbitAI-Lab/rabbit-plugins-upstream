## Description:

Paste a URL and use dLazy's hosted website-to-video agent to turn the page into a promo, social ad, or product demo video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and content teams use this skill when they have a webpage or landing-page URL and want an agent to create a promotional, advertising, or product demo video through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, target URLs, and attached files may be sent to dLazy's hosted API and media storage.

Mitigation: Avoid sensitive URLs or files unless the user is comfortable sharing them with dLazy and has appropriate authorization.

Risk: A dLazy API key may be saved in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable or the npx invocation when less local persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and service response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the pinned dLazy CLI invocation for the website-to-video template and may stream hosted agent responses.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

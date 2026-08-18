## Description:

Turns a supplied URL, webpage, or landing page into a promo, social ad, or product demo video by routing the task through the dLazy website-to-video template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill when they have a URL or landing page and want an agent to generate a promotional, advertising, or product demo video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, and files passed with --files may be sent to dLazy as an external SaaS.

Mitigation: Use this skill only when the user explicitly wants a webpage or link turned into a video, and avoid sending sensitive URLs or files unless approved for dLazy processing.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY when persistent storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project IDs, uploaded files, streamed task output, and generated video status or results.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

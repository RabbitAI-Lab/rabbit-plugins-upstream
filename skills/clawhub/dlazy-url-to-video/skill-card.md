## Description:

Turns a supplied URL into a promo, social ad, or product demo video through dLazy's hosted website-to-video agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to turn a webpage or landing-page URL into a generated promo, social ad, or product demo video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files may be sent to dLazy's hosted service.

Mitigation: Send only content intended for dLazy processing and avoid attaching sensitive local files unless approved.

Risk: Using a persistent global npm install leaves a third-party CLI on the system.

Mitigation: Use the pinned npx invocation when a persistent global binary is not needed.

Risk: The dLazy API key can remain available through local CLI config or environment variables.

Mitigation: Rotate or revoke the dLazy API key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides an agent to invoke the pinned dLazy CLI for a website-to-video project; attached files may be uploaded to dLazy media storage when used.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

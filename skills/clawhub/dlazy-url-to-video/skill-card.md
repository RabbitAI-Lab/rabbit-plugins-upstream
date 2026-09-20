## Description:

Turns a pasted webpage URL into a promo, social ad, or product demo video by capturing the page, deriving brand elements, storyboarding, adding voiceover, and building the video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn a website URL into a promotional, social ad, or product demo video through the hosted dLazy URL-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and attached files may be sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive websites or files unless permitted, and review dLazy's source and terms before use.

Risk: Login stores a dLazy API key in the local CLI configuration.

Mitigation: Use OS account protections, rotate or revoke keys as needed, or provide DLAZY_API_KEY per invocation when that better fits local policy.

Risk: A global install persists a third-party CLI on the system.

Mitigation: Use the pinned npx command for on-demand execution when a persistent global CLI is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash code blocks and CLI response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can start or continue dLazy projects and can upload attached files to dLazy-hosted storage when files are supplied.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter lists 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

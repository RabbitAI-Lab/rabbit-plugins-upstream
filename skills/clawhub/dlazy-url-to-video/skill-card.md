## Description:

Converts a supplied URL or webpage link into a promotional, social ad, or product demo video by capturing the site, deriving brand context, storyboarding, adding voiceover, and building the video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and agents use this skill when a user supplies a URL and wants a generated promotional, social ad, or product demo video through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, URLs, and explicitly attached files are sent to the dLazy service.

Mitigation: Use the skill only with content acceptable for third-party SaaS processing, and avoid sending sensitive URLs or files unless the account terms and user intent permit it.

Risk: The skill depends on running the third-party dLazy npm CLI.

Mitigation: Prefer the pinned npx invocation for one-off use, or review the package and source before installing a persistent global binary.

Risk: The skill requires a dLazy API key stored locally or supplied through the environment.

Mitigation: Keep the key scoped to the intended organization, avoid exposing it in prompts or logs, and rotate or revoke it if it is disclosed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated video work handled by the dLazy hosted service; requires a dLazy API key and a URL input.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

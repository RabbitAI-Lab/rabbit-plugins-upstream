## Description:

Turns a website URL into a promotional, advertising, or demo video with dLazy's website-to-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a supplied website or landing-page URL into a promotional video, social ad, or product demo through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website URLs, and attached files may be sent to dLazy.

Mitigation: Avoid submitting sensitive URLs or files and confirm the user is comfortable using the hosted service.

Risk: Authentication stores an API key in local CLI configuration.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: Using the dLazy service may consume paid credits.

Mitigation: Check credit availability and obtain user approval before paid use.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown with CLI commands and project updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation requires the dLazy service and an authenticated account.]

## Skill Version(s):

1.0.23 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

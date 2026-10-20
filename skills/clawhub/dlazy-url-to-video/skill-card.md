## Description:

Turns a webpage URL into a promotional, social ad, or product demo video using dLazy's hosted video creation service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers use this skill to turn a website or landing-page URL into a promotional video, social ad, or product demo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and task options are sent to dLazy's hosted service.

Mitigation: Review URLs and prompt contents before sending sensitive information.

Risk: Files explicitly attached to a task may be uploaded to dLazy.

Mitigation: Attach only files approved for sharing with the service.

Risk: Logging in or setting an API key stores the credential locally.

Mitigation: Protect local credentials and rotate or revoke the key if exposed.

Risk: Video generation may require paid credits.

Mitigation: Check the organization's credit balance and expected charges before running tasks.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with video results and links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation and project follow-up use dLazy's hosted service.]

## Skill Version(s):

1.0.28 (source: server-resolved ClawHub release; supplied skill frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

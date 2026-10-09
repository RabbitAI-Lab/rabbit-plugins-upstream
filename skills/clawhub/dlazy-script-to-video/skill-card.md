## Description:

Turns scripts into storyboarded, shot-by-shot videos by planning scenes, generating shots, assembling them, and checking the result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn a screenplay or scene outline into a multi-shot animated short with consistent characters, audio, and subtitles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files may be uploaded to the third-party dLazy service.

Mitigation: Avoid attaching sensitive files unless you intend to send them to dLazy.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Protect local credentials and rotate or revoke the key if compromised.

Risk: Running the skill requires a third-party npm CLI.

Mitigation: Review the package or source before installation; use the documented npx option to avoid a persistent global install.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Streaming text responses with project and generation updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides a hosted workflow for storyboard planning, shot generation, and video assembly.]

## Skill Version(s):

1.0.23 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

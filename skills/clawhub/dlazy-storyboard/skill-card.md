## Description:

Helps create multi-shot animated shorts with consistent characters, from script and shot planning through audio, subtitles, and video assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and produce multi-shot animated shorts with consistent characters through the dLazy storyboard service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected attachments are sent to the third-party dLazy service.

Mitigation: Send only prompts and files you intend to share with dLazy.

Risk: Login can store a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key through the dLazy dashboard when needed.

Risk: Installing the CLI globally leaves a persistent third-party tool on the machine.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` if a global install is not desired.

## Reference(s):

- [ClawHub storyboard skill](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text with storyboard guidance and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based sessions can continue across turns.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

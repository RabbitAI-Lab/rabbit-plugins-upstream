## Description:

A structured skill for planning multi-platform social-media visuals and copy across Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and related platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan platform-specific social-media image concepts, safe-area checks, in-image text, captions, and optional CLI-backed visual generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to the third-party dLazy API and media storage.

Mitigation: Use the skill only when the user is comfortable sending that content to dLazy, and avoid submitting sensitive or restricted media.

Risk: The dLazy CLI requires an API key that can be stored in a local configuration file.

Mitigation: Prefer the DLAZY_API_KEY environment variable when persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install creates a long-lived local CLI dependency.

Mitigation: Use the pinned npx command for on-demand execution or review the CLI source before installing globally.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with structured design plans, captions, checks, and inline shell commands when generation is requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated media URLs returned by the dLazy CLI.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

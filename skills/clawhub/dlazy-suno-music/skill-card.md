## Description:

Generates music with or without vocals using inspiration mode for automatic lyrics or custom mode for supplied lyrics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate vocal or instrumental music from prompts, with optional custom lyrics and style controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media files are sent to the third-party dLazy service.

Mitigation: Review prompts and media for sensitive content before submission.

Risk: The CLI uses a dLazy API key for hosted generation.

Mitigation: Protect the key, and rotate or revoke it through the dLazy dashboard if exposed.

Risk: Execution depends on the third-party dLazy CLI package.

Mitigation: Review the pinned CLI package and source before installation when stronger supply-chain assurance is needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands and JSON result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Hosted generation returns media URLs or an asynchronous task ID; optional local download.]

## Skill Version(s):

1.3.22 (source: ClawHub release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

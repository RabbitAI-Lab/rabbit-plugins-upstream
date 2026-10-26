## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn film, advertising, short-video, and educational briefs into staged storyboard plans, scripts, and rendered visual sequences.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and uploaded reference media are processed by dLazy for cloud rendering.

Mitigation: Use the service only when its processing is acceptable for the material; avoid uploading sensitive media without authorization.

Risk: The skill stores an API key in local CLI configuration when authenticated, and documented CLI install versions are inconsistent.

Mitigation: Prefer device-code login over putting a key directly in a command, and verify the intended CLI package version before installation; this card does not certify the external CLI implementation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI project homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Images, PDF]

**Output Format:** [Bulleted Markdown plans and storyboard scripts, image-generation requests and results, and print/PDF storyboard layouts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific panel counts, aspect ratios, shot metadata, and layout; staged user-confirmation gates before generation]

## Skill Version(s):

1.3.35 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

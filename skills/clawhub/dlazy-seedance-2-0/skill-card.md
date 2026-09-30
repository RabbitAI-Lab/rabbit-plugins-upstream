## Description:

Helps agents request video generation from text prompts, media references, or first and last frames using dLazy's Seedance 2.0 CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate videos from prompts and optional image, video, audio, or frame references through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's cloud service.

Mitigation: Review prompts and media for sensitive content before submitting them.

Risk: Login stores a dLazy API key locally.

Mitigation: Protect the local key and rotate or revoke it from the dLazy dashboard if needed.

Risk: A globally installed CLI persists on the machine.

Mitigation: Use the pinned npx invocation if a persistent global installation is undesirable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI repository (skill-declared link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands and generated asset URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task ID instead of a completed asset URL.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

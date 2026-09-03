## Description:

Fast version of ByteDance's Seedance 2.0 that generates videos faster with support for multi-modal references, first and last frames, and text-to-video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and content creators use this skill to generate Seedance 2.0 Fast videos through the dLazy CLI from text prompts and optional image, video, audio, first-frame, or last-frame references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced local media are sent to dLazy cloud endpoints.

Mitigation: Use only inputs intended for cloud processing and avoid sensitive local media unless upload to dLazy is acceptable.

Risk: The dLazy CLI can store an API key in ~/.dlazy/config.json.

Mitigation: Prefer the per-invocation DLAZY_API_KEY option or manually verify and restrict config file permissions after login.

Risk: The security verdict is suspicious because local API-key storage protection is overstated.

Mitigation: Review the scanner summary, CLI behavior, and deployment environment before approving the skill for use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0-fast)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files]

**Output Format:** [JSON command output with hosted media URLs; optional saved media file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generateId task for later polling.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

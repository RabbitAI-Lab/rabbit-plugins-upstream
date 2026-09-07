## Description:

Generate coherent transition videos from supplied first and last frame images using Jimeng's first-tail frame video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative operators use this skill to generate transition videos from a prompt plus first-frame and last-frame images through the dLazy Jimeng video-generation service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud video-generation service that requires credentials and uploads local media supplied by the user.

Mitigation: Use a revocable dLazy API key, avoid passing sensitive media, and confirm that uploaded files are intended for dLazy processing before invocation.

Risk: Installing a global CLI can introduce ordinary package supply-chain exposure.

Mitigation: Prefer the pinned npx invocation or an isolated environment, and review the linked package or source before installation.

Risk: The artifact documentation may contain mismatched examples or output descriptions for this first-frame/last-frame video workflow.

Mitigation: Verify current CLI help and use the documented firstFrame and lastFrame parameters before relying on generated command examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown instructions with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be returned as hosted file URLs or saved locally through the dLazy CLI.]

## Skill Version(s):

1.3.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

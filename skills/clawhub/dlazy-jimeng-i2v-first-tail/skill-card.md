## Description:

Generate coherent transition videos using Jimeng's first and tail frame models from supplied first-frame and last-frame images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to run the dLazy Jimeng first-tail image-to-video workflow, producing a transition video from a prompt plus first and last frame images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs an external npm CLI.

Mitigation: Prefer the pinned npx invocation or a sandboxed environment, and review the referenced CLI source or npm package before global installation.

Risk: Prompts, generation parameters, and selected media are sent to dLazy hosted services.

Mitigation: Avoid sensitive inputs unless the dLazy service terms and data handling are acceptable for the use case.

Risk: A dLazy API key is required and may be stored in the local CLI configuration.

Mitigation: Use a revocable API key, restrict local config access to the current OS user, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI can return hosted result URLs, async task identifiers, or save generated media to a requested local path.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

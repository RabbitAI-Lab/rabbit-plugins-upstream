## Description:

PixVerse C1 generates videos from text prompts, image inputs, first/last frames, and reference images through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to request PixVerse C1 video generations from prompts and optional reference media. It is suited for action, VFX, high-motion, image-to-video, and first/last-frame video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files supplied to the skill may be sent to dLazy services for generation.

Mitigation: Use the skill only for intended PixVerse C1 work and avoid submitting unrelated private files, confidential media, or secrets.

Risk: The skill requires a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use a revocable key, rotate or revoke it when needed, and prefer per-invocation environment variables when persistent local storage is undesirable.

Risk: A global CLI install persists a local executable and dependencies.

Mitigation: Prefer npx or a restricted execution environment when a persistent global CLI is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with bash commands; invoked CLI responses are JSON with generated media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; local media paths supplied to generation commands may be uploaded to dLazy services.]

## Skill Version(s):

1.2.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

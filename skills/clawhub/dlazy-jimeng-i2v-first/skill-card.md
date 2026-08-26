## Description:

Generates dynamic videos from a single first-frame image and prompt using Jimeng.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI for Jimeng first-frame image-to-video generation from prompts and an input image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image paths or media are sent to dLazy hosted services for generation.

Mitigation: Use only prompts and media approved for dLazy processing, and avoid submitting sensitive or restricted content.

Risk: dLazy login can store an API key locally in ~/.dlazy/config.json.

Mitigation: Protect the local config file, prefer per-invocation DLAZY_API_KEY where appropriate, and rotate or revoke the key from dLazy if exposure is suspected.

Risk: A global CLI install persists the dLazy executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted generated-media URLs, save an output asset with --save, or return an async generateId for polling.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

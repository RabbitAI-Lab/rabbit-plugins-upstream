## Description:

Generates ElevenLabs eleven_v3 multi-voice dialogue audio through the dLazy CLI, assigning voices per line and supporting expressive audio tags for character dialogue, podcasts, and short skits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate multi-speaker dialogue audio from structured dialogue lines, with optional language, stability, seed, async, and save controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and media paths may be sent to dLazy for cloud generation.

Mitigation: Avoid submitting sensitive content unless the dLazy service terms and data-handling posture are acceptable for the use case.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Protect the local config file and rotate or revoke the key from the dLazy dashboard when access should change.

Risk: The artifact documentation contains quality issues around example parameters and output type.

Mitigation: Confirm current command behavior with `dlazy elevenlabs-dialogue -h` or `--dry-run` before relying on examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy command may return generated asset URLs, async task IDs, or saved local files depending on flags such as --no-wait and --save.]

## Skill Version(s):

1.3.19 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

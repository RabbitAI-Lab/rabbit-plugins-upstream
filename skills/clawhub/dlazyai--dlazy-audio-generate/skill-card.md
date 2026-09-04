## Description:

Audio generation skill that selects an appropriate dLazy CLI audio or TTS model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate speech, dialogue, music, and sound effects through dLazy-hosted audio models from natural-language prompts and selected media inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and any explicitly passed media files are sent to a third-party hosted generation service.

Mitigation: Avoid submitting sensitive prompts or local media unless the transfer to dLazy is intended and permitted for the use case.

Risk: The dLazy API key may be stored in the local user configuration file.

Mitigation: Use a revocable API key, protect the local config file, and rotate or revoke the key when access is no longer needed.

Risk: Generation requests may consume account credits.

Mitigation: Confirm account balance and intended model selection before running commands that create paid generation jobs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned through dLazy-hosted output URLs when commands complete successfully.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

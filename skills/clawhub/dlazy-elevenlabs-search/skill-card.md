## Description:

Searches the ElevenLabs voice library by keyword, source, and category and returns playable preview links for matching voices before TTS use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to search ElevenLabs voices through the dLazy CLI, filter by source or category, and select a previewable voice before running TTS.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party cloud CLI and requires a dLazy API key.

Mitigation: Review the skill before installing, prefer per-run DLAZY_API_KEY where practical, and check permissions on ~/.dlazy/config.json after login.

Risk: Voice search prompts and parameters are sent to dLazy API endpoints.

Mitigation: Avoid sending sensitive prompts or identifiers unless the user accepts dLazy cloud processing for the task.

Risk: The artifact documentation shows an image-style output example that does not match the expected voice search behavior.

Mitigation: Expect voice search results and preview URLs, and validate command output before relying on downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [JSON from the dLazy CLI, with text guidance for command usage and authentication errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice search results are expected to include matching voices and playable preview URLs; async mode may return a task identifier.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

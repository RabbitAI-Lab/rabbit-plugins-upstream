## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews so users can choose a voice before TTS use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to search available ElevenLabs voices by prompt, source, category, and result count before selecting a voice for text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external dLazy npm CLI and hosted API that receive prompts and search parameters.

Mitigation: Review the dLazy CLI before use, prefer npx or an isolated environment for testing, and only run the skill when sharing prompts and parameters with dLazy is acceptable.

Risk: Authentication uses a dLazy API key that may be stored in local CLI configuration.

Mitigation: Use account-scoped keys, protect the local configuration file, and rotate or revoke the key from the dLazy dashboard when access should change.

Risk: The skill includes mandatory guidance for recharge and API-key setup when service errors occur.

Mitigation: Review agent behavior around billing and credential prompts before deployment, and ensure users explicitly approve payment or credential setup actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Service Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include playable preview URLs or asynchronous task status from the dLazy CLI.]

## Skill Version(s):

1.3.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

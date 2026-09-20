## Description:

Search the ElevenLabs voice library by keyword, source, and category, returning playable previews so users can choose a voice before running TTS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and voice workflow operators use this skill to search ElevenLabs voices by prompt, source, category, and result count before selecting a voice for text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends search prompts and parameters to dLazy's hosted API and requires dLazy authentication.

Mitigation: Confirm trust in the dLazy CLI and hosted service before use; prefer per-run DLAZY_API_KEY authentication when you do not want credentials saved in ~/.dlazy/config.json.

Risk: The documentation contains copy-paste inconsistencies, including an image/png output example and image/video error text for a voice-search workflow.

Mitigation: Treat those examples as documentation issues to clarify with the publisher rather than expected ElevenLabs voice-search behavior.

Risk: Global installation leaves a persistent CLI on the system.

Mitigation: Use the documented npx @dlazy/cli@1.2.3 invocation when you want on-demand execution without a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-search)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned @dlazy/cli invocation and may return asynchronous task status when --no-wait is used.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

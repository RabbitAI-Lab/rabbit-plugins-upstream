## Description:

This skill uses dLazy's hosted ElevenLabs eleven_v3 text-to-speech service to generate multilingual speech with curated voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create speech audio for dubbing, audiobooks, and character dialogue through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected inputs are sent to dLazy's hosted service, and generated outputs are hosted by dLazy.

Mitigation: Review data sensitivity and service terms before use; avoid sending confidential or regulated content unless approved for dLazy processing.

Risk: The dLazy CLI may store an API key in a local user configuration file.

Mitigation: Use the DLAZY_API_KEY environment variable when persistent local storage is not appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Local file paths passed to supported media fields may be uploaded to dLazy media storage.

Mitigation: Only pass files intended for cloud processing and confirm that upstream pipeline references do not include unintended local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Configuration instructions]

**Output Format:** [JSON result with hosted output URLs; optional downloaded media file via --save]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation with --no-wait and status polling by generateId.]

## Skill Version(s):

1.3.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

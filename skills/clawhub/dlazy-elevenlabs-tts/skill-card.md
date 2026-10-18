## Description:

Guides agents to generate ElevenLabs text-to-speech audio through dLazy, with multilingual voice and delivery controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn text into spoken audio for dubbing, audiobooks, and character dialogue through the dLazy-hosted ElevenLabs service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text and selected settings are sent to a third-party hosted service.

Mitigation: Avoid sending confidential text or parameters unless approved for the service.

Risk: A dLazy API key is stored locally when using CLI login or auth commands.

Mitigation: Protect the local configuration or use a per-session environment variable; rotate or revoke the key if exposed.

Risk: The skill's example labels a text-to-speech result as an image, which can mislead users about the returned asset.

Mitigation: Verify the actual asset type before using or sharing the output; correct the example to show audio.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the pinned package and listed source before installing in environments with stricter supply-chain requirements.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with shell commands; CLI returns JSON with generated asset links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service generates audio; asynchronous requests may return a task ID before an asset is ready.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

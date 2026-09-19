## Description:

语音合成 ElevenLabs TTS helps agents call the dLazy ElevenLabs TTS CLI to generate speech from prompts with curated multilingual voices and stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to create multilingual text-to-speech audio for dubbing, audiobooks, and character dialogue through the dLazy-hosted ElevenLabs TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected TTS options are sent to a third-party cloud API.

Mitigation: Review prompt sensitivity before use and avoid submitting confidential or regulated content unless the dLazy service is approved for that data.

Risk: Authentication stores a dLazy API key in local CLI configuration or accepts it through an environment variable.

Mitigation: Protect the local config file, prefer scoped keys, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: The skill depends on a third-party npm CLI and hosted service endpoints.

Mitigation: Review the pinned @dlazy/cli package before installation and confirm expected communication with api.dlazy.com and files.dlazy.com.

Risk: The documentation includes a copied media-output example that shows image output for a speech tool.

Mitigation: Validate actual dlazy elevenlabs-tts help and runtime output before integrating the skill into automated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI metadata link](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [CLI JSON result with generated asset URLs or async task status; the --save option can write the generated asset to a local file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and network access to dLazy API and file-hosting endpoints.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

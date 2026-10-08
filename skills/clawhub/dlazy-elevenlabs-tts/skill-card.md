## Description:

Generates multilingual speech with ElevenLabs eleven_v3 through the dLazy CLI, with selectable voices and controls for stability, similarity, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn scripts into speech for dubbing, audiobooks, and character dialogue, selecting from curated or custom voices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external npm CLI and using dLazy account credentials introduces dependency and credential exposure risks.

Mitigation: Review the pinned CLI package before installing, protect the API key, and rotate or revoke it if exposed.

Risk: Prompts and file paths intentionally passed to media fields may be uploaded to dLazy.

Mitigation: Only submit content and local files approved for the external service.

Risk: The documented sample result appears copied from an image tool and may misrepresent TTS output.

Mitigation: Verify the returned asset type and audio playback before using or sharing results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-tts)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Audio result links]

**Output Format:** [Text with shell commands and hosted audio result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved locally; verify the actual audio output because the documented sample shows an image result.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

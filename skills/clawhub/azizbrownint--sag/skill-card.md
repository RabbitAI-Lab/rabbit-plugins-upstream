## Description:

ElevenLabs text-to-speech with mac-style say UX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use sag to turn chat responses or supplied text into ElevenLabs speech with local playback, voice selection, and delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice text is sent to ElevenLabs under the user's API key.

Mitigation: Avoid using voice replies for secrets or sensitive personal data, and review ElevenLabs handling requirements before use.

Risk: The skill depends on the sag CLI installed from the listed Homebrew tap.

Mitigation: Install only if the Homebrew tap and sag binary are acceptable for the user's environment.

Risk: Generated MP3 files may remain in /tmp after playback or sharing.

Mitigation: Clean up generated /tmp audio files when local retention matters.

## Reference(s):

- [sag homepage](https://sag.sh)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/sag)
- [Publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, audio files]

**Output Format:** [Markdown guidance with inline shell commands and generated MP3 media references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the sag CLI with an ElevenLabs API key; generated voice replies may be written to /tmp as MP3 files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

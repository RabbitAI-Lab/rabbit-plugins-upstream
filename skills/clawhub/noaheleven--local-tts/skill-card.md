## Description:

Converts text into local speech audio files using edge-tts by default, Azure Speech for expanded Chinese voice coverage, and pyttsx3 as an offline fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to synthesize text into MP3 or WAV narration, voice-over, and spoken-summary audio files, with cloud and offline paths available depending on sensitivity and connectivity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default cloud synthesis can send submitted text to Microsoft-operated TTS services.

Mitigation: Use --offline for sensitive text and review data-handling requirements before sending content to cloud TTS providers.

Risk: The Azure helper appears broken as packaged according to the server security summary.

Mitigation: Fix or review scripts/azure_tts.py before relying on the Azure channel.

Risk: Azure Speech credentials are read from local environment or key files.

Mitigation: Keep Azure keys out of version control, restrict access to credential files, and rotate keys if exposure is suspected.

## Reference(s):


## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands; generated audio files are MP3 or WAV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud modes may call Microsoft-operated TTS services; offline mode uses pyttsx3 where available.]

## Skill Version(s):

1.1.0 (source: frontmatter and changelog, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Helps users list VoiceLabs voice profiles, add built-in voices, choose a voice for a language, and clone a consenting speaker's voice from a recording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

VoiceLabs users can review their voice library, add preset voices, select voices for languages, and create a cloned voice when the speaker has consented.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloning without permission could create a reusable copy of another person's voice.

Mitigation: Confirm that the speaker is the user or has explicitly consented before cloning; do not clone unconsenting speakers or public figures.

Risk: A recording or audio URL is sent to VoiceLabs and stored as a reusable voice profile.

Mitigation: Explain this transfer and persistence before cloning, and use built-in preset voices when a custom clone is unnecessary.

## Reference(s):

- [VoiceLabs: Managing Voice Library on ClawHub](https://clawhub.ai/bsalaeddin/skills/voicelabs-managing-voice-library)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice listings and profile details, with creation status and profile ID when applicable.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

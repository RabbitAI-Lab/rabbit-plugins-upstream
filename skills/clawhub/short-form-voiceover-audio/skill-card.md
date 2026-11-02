## Description:

Creates editable AI voiceover audio from finalized short-video scripts, with voice, pronunciation, pacing, and duration controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and short-form video teams use this skill to turn finalized scripts into editable narration for social videos, explainers, reviews, and ads. They can select a supported voice and language, tune pronunciation and pacing, review the current price estimate, and check returned audio duration against the target edit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization covers Beatra media and spending permissions beyond an audio-only task, including voice modification.

Mitigation: Review the requested account scope before authorizing and revoke the shared connection in the Beatra Console when needed.

Risk: The submitted script is sent to Beatra, and installation analytics are sent automatically.

Mitigation: Consider whether the script contains sensitive information and account for automatic installation analytics before use.

Risk: Voiceover generation can incur credit charges.

Mitigation: Review the current estimate and approve the exact quoted job before generating audio.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/short-form-voiceover-audio)
- [Beatra skill page](https://beatra.ai/skills/short-form-voiceover-audio)

## Skill Output:

**Output Type(s):** [Audio, Text]

**Output Format:** [MP3 voiceover audio with textual task status and usage details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio duration varies with the script and delivery settings; generation may consume Beatra credits.]

## Skill Version(s):

0.2.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

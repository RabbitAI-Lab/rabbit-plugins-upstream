## Description:

Turns user-provided text into speech using a VoiceLabs voice and returns a temporary audio link.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

VoiceLabs users convert approved text, scripts, or multi-part documents into spoken audio using their voice profiles and receive links to the generated audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text submitted for speech generation is sent to VoiceLabs.

Mitigation: Send only text the user provided or approved, and avoid confidential text unless the account's data terms are suitable.

Risk: Hosted audio links expire after about 15 minutes.

Mitigation: Request a fresh link for a completed generation if the original has expired.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/voicelabs-reading-text-aloud)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Markdown with audio links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio links expire after about 15 minutes; generation is metered by the user's plan.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

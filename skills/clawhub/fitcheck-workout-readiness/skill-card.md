## Description:

Guides users to a browser-based EmoCity scan for workout readiness, stress, emotion, composure, eye contact, micro-expression, voice cue, and heart-rate-estimate feedback, with on-device browser scanning for live camera sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

PROPRIETARY

## Use Case:

External users and agents use this skill to guide consent-based EmoCity scans, explain the resulting stress, emotion, composure, eye-contact, micro-expression, voice-cue, and heart-rate-estimate readings, and frame them as entertainment or self-insight rather than medical, psychological, forensic, screening, or lie-detection evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera, microphone, uploaded media, biometric, emotion, stress, composure, and heart-rate-estimate features are privacy-sensitive.

Mitigation: Use the skill only with informed consent, avoid uploading or sharing another person's media without permission, and treat exported summaries as sensitive.

Risk: Composure, deception, stress, emotion, voice, and heart-rate estimates may be mistaken for medical, psychological, forensic, screening, or lie-detection evidence.

Mitigation: Frame results as entertainment and self-insight only, describe readings as loose tendencies, and never use scans to judge or make decisions about a person.

Risk: Exported or account-saved summaries can still reveal sensitive personal signals even when raw video or audio is not shared.

Mitigation: Share only aggregated summaries intentionally, keep reports private by default, and remind users that signed-in summaries may be saved to their own account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gv66co/skills/fitcheck-workout-readiness)
- [EmoCity app](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse](https://www.emopulse.app)
- [EmoPulse Face Signals API](https://rapidapi.com/emocity/api/emopulse-face-analysis)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown guidance with concise interpretation text and user-facing safety reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs users to browser, upload, or challenge workflows and helps interpret scan summaries without treating them as verdicts.]

## Skill Version(s):

1.1.3 (source: frontmatter, clawhub.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

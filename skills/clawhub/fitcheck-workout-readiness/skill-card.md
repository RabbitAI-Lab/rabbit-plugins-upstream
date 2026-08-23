## Description:

Camera check-in for training days: stress, recovery, mood, and a heart-rate estimate before or after a workout, with on-device browser analysis and wellness guidance that is not medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

PROPRIETARY

## Use Case:

External users and wellness-oriented developers use this skill to guide browser-based camera, microphone, or uploaded-media check-ins for stress, mood, composure, and workout-readiness signals. It is intended for self-insight and entertainment, not medical, psychological, employment, forensic, or lie-detection decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill involves sensitive camera, microphone, and biometric analysis.

Mitigation: Use it only for yourself or with clear consent from every person in the camera feed, audio, photo, or video.

Risk: Users may overread stress, composure, authenticity, voice, or heart-rate estimates as medical, psychological, forensic, employment, or lie-detection evidence.

Mitigation: Frame outputs as loose wellness or entertainment signals and avoid decisions that depend on clinical, legal, employment, or truthfulness claims.

Risk: Privacy expectations may differ across on-device scans, analytics, sharing/export features, and the separate RapidAPI media-upload workflow.

Mitigation: Review privacy implications before use, share only summaries intentionally, and treat uploaded media workflows separately from the browser-only scan flow.

Risk: Weak lighting, camera angle, noise, low signal quality, or experimental voice and rPPG estimates can produce unreliable readings.

Mitigation: Treat individual numbers as tendencies, check signal quality, and repeat scans under better conditions before drawing even informal conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gv66co/skills/fitcheck-workout-readiness)
- [EmoCity live app](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse](https://www.emopulse.app)
- [EmoPulse Face Signals API](https://rapidapi.com/emocity/api/emopulse-face-analysis)

## Skill Output:

**Output Type(s):** [guidance, markdown, text]

**Output Format:** [Markdown-style user guidance with plain-language interpretation of biometric signal summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference stress, mood, composure, heart-rate estimate, eye contact, voice cue, micro-expression, signal-quality, and export-summary results when users provide them.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, clawhub.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

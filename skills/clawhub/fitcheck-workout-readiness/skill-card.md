## Description:

Workout readiness and recovery check from a 60-second face scan in the browser: stress, mood, composure and a heart-rate estimate before or after training, a hard call or a date, with before-and-after comparisons. Also a deception challenge to play with friends and a video read. The scan runs on-device and no video or audio leaves the device. With the person's own RapidAPI key it can also analyse a photo they hand over, uploaded on purpose with their consent. Self-insight and entertainment, not a medical or lie-detection tool. Powered by EmoPulse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

PROPRIETARY

## Use Case:

External users use this skill to guide a browser-based workout readiness, stress, mood, composure, heart-rate, or before-and-after recovery check and to interpret results as tendencies. With a user's own RapidAPI key and explicit consent, the agent may also run a photo or clip analysis and explain the returned JSON in plain language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A real RapidAPI key could be exposed when the agent prepares or runs a shell command.

Mitigation: Use only the user's own key, avoid writing it into files or chat transcripts, and prefer a private environment variable or secret input path before running API calls.

Risk: Photo or clip analysis uploads biometric media to the EmoPulse API through RapidAPI.

Mitigation: Run uploaded-media analysis only after the user confirms they own or have consent for the media and understands that the file leaves the device.

Risk: Biometric readiness, stress, composure, or deception-style outputs may be overread as medical, employment, relationship, or truthfulness evidence.

Mitigation: Frame outputs as self-reflection or entertainment, explain low-signal limits, and avoid using results to screen, judge, diagnose, or decide about people.

## Reference(s):

- [EmoCity live app](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse Face Analysis API](https://rapidapi.com/emocity/api/emopulse-face-analysis)
- [EmoPulse](https://www.emopulse.app)
- [EmoCity on Google Play](https://play.google.com/store/apps/details?id=city.emo.www.twa&referrer=utm_source%3Dclawhub%26utm_medium%3Dskill)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, API calls]

**Output Format:** [Plain-language guidance and Markdown, with optional curl commands and JSON response interpretation for consented RapidAPI analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Browser scans produce user-facing summaries; optional API analysis returns per-face JSON that the agent should treat as tendencies, not verdicts.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter, clawhub.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

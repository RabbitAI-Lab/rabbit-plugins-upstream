## Description:

Face scan from the browser camera in 60 seconds: stress, a heart-rate estimate, mood, micro-expressions, eye contact, genuine smile, composure and, with the microphone on, voice tension, as a summary the agent turns into JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to run or interpret FitCheck face-scan summaries for workout readiness, stress checks, before-and-after comparisons, friend challenges, and optional user-provided photo or clip analysis. The agent turns pasted scan summaries or API responses into concise JSON, short reads, and challenge scoreboards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face, mood, stress, voice-tension, and optional media-upload analysis can involve sensitive biometric or emotion data.

Mitigation: Use only with the subject's explicit agreement, treat readings as entertainment or wellness signals, and avoid medical, employment, insurance, law-enforcement, or truth-detection decisions.

Risk: The optional RapidAPI path uploads a user-selected photo or clip to a third-party service.

Mitigation: Use the upload path only after the user confirms the file, understands that it will be uploaded, and provides their own RapidAPI key through the environment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gv66co/skills/fitcheck-workout-readiness)
- [emo.city FitCheck homepage](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse Face Analysis API](https://rapidapi.com/emocity/api/emopulse-face-analysis)
- [EmoPulse](https://www.emopulse.app)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown prose with JSON objects and optional bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain before-and-after comparisons or challenge scoreboards in conversation; optional API use can upload a user-selected media file after explicit consent.]

## Skill Version(s):

1.3.0 (source: SKILL.md frontmatter, clawhub.json, evidence.json release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

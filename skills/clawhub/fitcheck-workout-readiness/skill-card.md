## Description:

Guides consent-based face scans and returns short summaries of estimated stress, heart rate, mood, and related expression signals for wellness check-ins and games.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

MIT-0

## Use Case:

External users can request a camera-based check-in, compare before-and-after readings, or play a consent-based challenge with friends. An optional path analyzes a user-provided photo or video through EmoPulse after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A face or voice scan may involve someone who has not consented.

Mitigation: Use only when everyone being scanned has agreed.

Risk: Stress, heart-rate, mood, or deception-style estimates may be mistaken for medical findings or proof of truthfulness.

Mitigation: Present readings as entertainment or wellness signals, not medical advice or lie-detection results.

Risk: Optional photo or video analysis uploads the selected file to EmoPulse through RapidAPI.

Mitigation: Explain the upload, obtain explicit confirmation, and use a dedicated revocable user-provided key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gv66co/skills/fitcheck-workout-readiness)
- [Emocity browser scan](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse Face Analysis API](https://rapidapi.com/emocity/api/emopulse-face-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-language summary and structured JSON scan readings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include before-and-after changes or a challenge scoreboard.]

## Skill Version(s):

1.5.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

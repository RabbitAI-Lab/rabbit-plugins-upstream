## Description:

Guides users through a browser-based face scan and turns their pasted results into structured summaries and comparisons, with optional consent-based photo or video analysis through EmoPulse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gv66co](https://clawhub.ai/user/gv66co)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals use the skill to summarize their own face-scan results, compare scans before and after an activity, or run consensual challenges with friends. They may also request analysis of a photo or clip they provide using their own API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Biometric and mood scans can involve sensitive information about people who did not consent.

Mitigation: Scan only yourself or people who clearly agreed to participate.

Risk: Stress, mood, heart-rate, genuineness or deception scores may be mistaken for medical or truthfulness determinations.

Mitigation: Treat results as estimates or entertainment, not diagnoses or evidence of deception.

Risk: Optional photo or video analysis uploads the selected media to EmoPulse through RapidAPI.

Mitigation: Use only media provided with consent, disclose the upload and wait for confirmation; use the user's own API key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/gv66co/skills/fitcheck-workout-readiness)
- [Emocity browser scan](https://emo.city?utm_source=clawhub&utm_medium=skill)
- [EmoPulse Face Analysis on RapidAPI](https://rapidapi.com/emocity/api/emopulse-face-analysis)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [Structured JSON with a brief plain-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include before-and-after changes or an in-conversation challenge scoreboard; unavailable heart-rate values are null.]

## Skill Version(s):

1.3.1 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

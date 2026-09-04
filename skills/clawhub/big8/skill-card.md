## Description:

Big8 helps agents provide entertainment-oriented Chinese fortune-telling guidance, including BaZi chart readings, feng shui and face-reading image analysis, zodiac and horoscope summaries, I Ching-style daily divination, and daily almanac readings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users use Big8 for entertainment-oriented Chinese metaphysics responses: BaZi readings from birth details, feng shui and face-reading from images, zodiac guidance, daily divination, and almanac summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to analyze selfies, faces, home interiors, birth dates, and birth times for entertainment-style fortune inferences.

Mitigation: Require explicit user intent before analyzing images or birth details, prefer captioned image requests, and keep results framed as entertainment rather than factual determinations.

Risk: Fortune-telling outputs could be mistaken for serious medical, financial, legal, relationship, or life advice.

Mitigation: Avoid high-stakes recommendations, state practical boundaries when relevant, and direct users to qualified professionals for consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/big8)
- [Publisher profile](https://clawhub.ai/user/kobenfang)
- [Artifact skill instructions](artifact/SKILL.md)
- [Artifact product plan](artifact/big8-plan.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown responses with structured sections; calculation helper results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may depend on user-provided images, birth dates, birth times, and the runtime date; readings should remain entertainment-oriented.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Big8 is a Chinese fortune-telling assistant for BaZi readings, feng shui and face-reading image analysis, horoscope lookup, daily hexagrams, and Chinese almanac guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

External users use Big8 for entertainment-style Chinese fortune-telling, including BaZi chart explanations, feng shui layout suggestions from room photos, face-reading from selfies, horoscope compatibility, daily hexagrams, and almanac checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process selfies, face images, and private room photos for entertainment-style analysis.

Mitigation: Use only with images the user is comfortable sharing with the active agent or vision system, and avoid third-party faces without permission.

Risk: The artifact makes broad privacy claims, while security evidence says image inference and retention details are unclear.

Mitigation: Treat privacy guarantees as unverified unless the publisher clarifies where image inference occurs and how long inputs are retained.

Risk: Fortune-telling, face-reading, feng shui, and almanac outputs can be mistaken for deterministic advice.

Mitigation: Present outputs as entertainment or cultural reference and avoid medical, legal, financial, or life-changing decisions based on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/big8)
- [Skill instructions](artifact/SKILL.md)
- [Big8 plan](artifact/big8-plan.md)
- [Big8 helper script](artifact/scripts/big8.py)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with occasional JSON helper-script outputs and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entertainment-style outputs; image modes depend on user-provided face or room photos and vision analysis.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

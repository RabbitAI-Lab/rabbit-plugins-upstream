## Description:

Helps drivers check tire pressure against vehicle placard settings, assess tread measurements, and track routine tire checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Drivers and vehicle-maintenance assistants use this skill to compare measured tire pressure with vehicle placard values, review tread-depth readings, and keep a monthly check history. Treat its calculated pressure targets as guidance, not a substitute for the vehicle manual or professional advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The altitude correction can produce unsafe pressure recommendations.

Mitigation: Do not rely on altitude-adjusted targets; use the vehicle placard and manual or consult a tire professional.

Risk: Tire-setting advice may omit important load, towing, high-speed, and TPMS-fault requirements.

Mitigation: Confirm vehicle-specific requirements in the manual or with a tire professional before changing settings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/voronindenis5/skills/tire-pressure-coach)
- [Tire Pressure Coach reference](references/tire-science.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, JSON files]

**Output Format:** [Plain text with local JSON check history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-tire pressure and tread verdicts and suggested check dates; stores measurements locally.]

## Skill Version(s):

1.0.1 (source: ClawHub release; bundled skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

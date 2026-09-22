## Description:

Personal health management and wellness assistant. Use when users want to track health data, get health advice, manage medications, analyze symptoms, get exercise/diet recommendations, or prepare for travel with health essentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[welliu](https://clawhub.ai/user/welliu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to track personal health data, manage medications and reminders, screen symptoms, and receive wellness, exercise, diet, first-aid, and travel-health guidance. The skill is informational and should not replace professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist sensitive health and medication details locally in plaintext under ~/.health_data.

Mitigation: Use only with informed consent, limit stored medical details, protect the local account and filesystem, and delete exported or retained data when no longer needed.

Risk: The skill provides medical, medication, first-aid, and emergency guidance that may be incomplete or locally inaccurate.

Mitigation: Treat outputs as informational, verify emergency numbers and medication decisions with local services and qualified clinicians, and escalate serious symptoms to professional care.

## Reference(s):

- [Common Health Conditions Reference](references/common_conditions.md)
- [Emergency First Aid Reference](references/first_aid.md)
- [Travel Health Preparation Checklist](references/travel_health.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with health guidance, checklists, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local JSON files for profile, medications, reminders, records, and goals when the helper scripts are used.]

## Skill Version(s):

1.0.0 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

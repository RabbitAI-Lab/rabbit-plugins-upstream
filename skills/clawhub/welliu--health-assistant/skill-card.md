## Description:

Health Assistant supports personal health tracking, medication reminders, symptom analysis, exercise and diet guidance, travel health preparation, first aid, international drug regulations, mental health support, and pet care.

This skill is ready for commercial/non-commercial use.

## Publisher:

[welliu](https://clawhub.ai/user/welliu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to organize personal wellness information, reminders, travel health preparation, first-aid lookups, mental-health support prompts, and pet-care guidance. It should be treated as informational support, not professional medical, veterinary, mental-health, legal, or emergency advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect sensitive medical details and store them in plaintext local JSON files under the user's home directory.

Mitigation: Disclose local storage before use, minimize sensitive entries, restrict file permissions, and provide review, export, and deletion steps for the stored health data.

Risk: Medical, emergency, mental-health, veterinary, and travel-regulation guidance may be incomplete, outdated, or unsafe for a user's location.

Mitigation: Require confirmation from qualified professionals or current official sources, and direct urgent or high-risk situations to local emergency services.

Risk: The security evidence flags weak disclosure and unclear controls for health data handling.

Mitigation: Review the skill before installation, document data handling plainly, and avoid using the storage scripts where consent, retention, or access controls are not acceptable.

## Reference(s):

- [Common Health Conditions Reference](references/common_conditions.md)
- [Emergency First Aid Reference](references/first_aid.md)
- [Travel Health Preparation Checklist](references/travel_health.md)
- [ClawHub Skill Page](https://clawhub.ai/welliu/skills/health-assistant)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional Python and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local JSON health data files when its bundled scripts are used.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

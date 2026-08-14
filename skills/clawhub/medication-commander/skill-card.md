## Description:

Manages medication schedules, detects drug interactions, tracks adherence, and generates refill reminders. Produces safe daily schedules and printable checklists from a medication list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and care-support agents use this skill to organize medication schedules, check a limited built-in interaction list, track dose adherence, and prepare refill reminders or printable daily checklists. It is for organization and reminders, not medical decision-making.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Medication names and adherence counts may be stored in a local JSON file under the user's home directory.

Mitigation: Install only if local storage of this medication history is acceptable, and handle the file according to the user's privacy requirements.

Risk: Interaction checks and scheduling guidance are limited and may be incorrect or incomplete for clinical decisions.

Mitigation: Use outputs for organization and reminders only, and confirm interaction warnings, dose changes, severe symptoms, or emergencies with a pharmacist, clinician, or emergency service.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/medication-commander)
- [GitHub Repository](https://github.com/voronindenis5/medication-commander)
- [GitHub Commit 9196814](https://github.com/voronindenis5/medication-commander/commit/9196814c6076cadac9bd6230abf803c14dfe3ef5)
- [Drug Interaction Database Reference](references/interactions.md)
- [Usage Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Guidance]

**Output Format:** [JSON for schedule, interaction, adherence, and refill commands; plain text for printable checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The adherence command stores medication names and adherence counts in a local JSON file under the user's home directory.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Track symptoms over time, correlate them with food, weather, medication, activity, sleep, and stress, detect patterns and flare-ups, and generate doctor-ready reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users can log symptoms, severity, notes, triggers, and medication mentions over time, then generate timelines, trigger correlations, flare-up summaries, heatmaps, and plain-text reports for medical appointments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local symptom data and exported reports may contain private medical information.

Mitigation: Store the database and reports in a protected location, review reports before sharing them, and delete exports that are no longer needed.

Risk: Generated correlations and summaries can be incomplete or misleading if logs are sparse, inconsistent, or entered incorrectly.

Mitigation: Use reports as appointment preparation material and review conclusions with a qualified clinician before making health decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/symptom-timeline)
- [Server-Resolved Source Repository](https://github.com/voronindenis5/symptom-timeline)
- [Symptom Tracking Guide](references/symptom-tracking-guide.md)
- [Doctor Visit Preparation](references/doctor-visit-prep.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [Plain text, terminal output, JSON database records, ASCII heatmaps, and exported text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local JSON storage by default and can export reports to a user-specified path.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

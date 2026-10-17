## Description:

Helps people explore Garmin Connect health, activity, and calendar data through natural-language questions, route analysis, and interactive dashboards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bolinches](https://clawhub.ai/user/bolinches)

### License/Terms of Use:

Apache 2.0

## Use Case:

Garmin Connect users can ask an agent to summarize sleep, recovery, workouts, and calendar entries, inspect activity routes, and create health dashboards. Trip changes can also be previewed and explicitly confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garmin account access exposes sensitive health, activity, location, travel, and profile data.

Mitigation: Use the skill only if that access is acceptable; avoid sharing outputs containing personal data.

Risk: Garmin credentials and saved sessions can be disclosed from shared configuration or local files.

Mitigation: Keep credentials out of shared files; delete ~/.openclaw/garmin to revoke the saved session.

Risk: Confirming a trip update or deletion can change Garmin calendar data.

Mitigation: Review the preview before explicitly confirming trip updates or deletions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bolinches/skills/garmin-health-analysis-2)
- [Garmin Connect API reference](artifact/references/api.md)
- [Health analysis guide](artifact/references/health_analysis.md)
- [Extended capabilities](artifact/references/extended_capabilities.md)
- [garminconnect Python library](https://github.com/cyberjunky/python-garminconnect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, HTML dashboards, Activity files]

**Output Format:** [Natural-language responses, command examples, HTML charts, and downloadable FIT/GPX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personal Garmin health and location data may be included in responses or files.]

## Skill Version(s):

1.6.0 (source: frontmatter, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

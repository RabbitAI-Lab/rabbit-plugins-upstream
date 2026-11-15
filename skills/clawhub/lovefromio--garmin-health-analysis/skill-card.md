## Description:

This skill lets users query Garmin Connect health and activity data, interpret trends, and generate interactive health charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovefromio](https://clawhub.ai/user/lovefromio)

### License/Terms of Use:

MIT-0

## Use Case:

External Garmin users can ask an agent to retrieve and summarize sleep, recovery, heart-rate, activity, and other health metrics, explore trends, and create charts. The skill also supports time-based activity queries and FIT or GPX downloads for route analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The credential example passes a password on the command line.

Mitigation: Use the documented environment-variable or local-config options instead, and avoid placing a real password in a command.

Risk: An ambiguous question may trigger retrieval of health data.

Mitigation: Clarify the requested metric and date range before retrieving health data.

Risk: A profile query may include account identity information.

Mitigation: Retrieve profile data only when needed and limit identity details in responses.

## Reference(s):

- [Health analysis guide](references/health_analysis.md)
- [Garmin Connect API reference](references/api.md)
- [Extended capabilities](references/extended_capabilities.md)
- [garminconnect Python library](https://github.com/cyberjunky/python-garminconnect)
- [Garmin Connect](https://connect.garmin.com)

## Skill Output:

**Output Type(s):** [Text, Analysis, JSON, HTML charts, FIT/GPX files, Guidance]

**Output Format:** [Natural-language responses, JSON data, interactive HTML charts, and FIT or GPX activity files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain personal health and activity information; health interpretations are informational and not medical advice.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

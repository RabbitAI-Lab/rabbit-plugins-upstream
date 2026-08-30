## Description:

Analyzes fixed-camera reptile enclosure video to produce hourly activity measurements, circadian rhythm alignment, anomaly alerts, and husbandry guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, keepers, breeders, and researchers use this skill to analyze 24-hour or multi-day reptile enclosure footage, compare observed activity with species rhythm baselines, and generate structured rhythm reports. It supports history lookup and report export for previously analyzed enclosure records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure videos, video URLs, report history, and account identifiers may be sent to a configured remote service.

Mitigation: Review data handling before installation, use trusted HTTPS production endpoints, and document retention and cleanup for uploaded media, report data, identities, and tokens.

Risk: Private or development HTTP endpoints can expose uploaded media, report history, or tokens if used outside a controlled environment.

Mitigation: Replace private development endpoints with trusted HTTPS production endpoints before normal use.

Risk: Circadian conclusions may be misleading when footage is incomplete, the camera is unstable, IR night vision is unavailable, light schedules are missing, or species rhythm/context data is absent.

Mitigation: Require complete fixed-camera 24-hour footage, IR night vision, recorded light schedule, species rhythm label, and relevant physiological context; mark poor inputs as unreliable.

## Reference(s):

- [Skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured JSON or Markdown report text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call a remote service to analyze local video files or video URLs and retrieve report history.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

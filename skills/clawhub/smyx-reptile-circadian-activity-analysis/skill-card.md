## Description:

Analyzes fixed-camera reptile enclosure video to measure hourly activity, compare activity patterns with species circadian baselines, and produce a structured rhythm report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and reptile husbandry operators use this skill to analyze 24-hour enclosure videos, identify activity peaks, detect day-night rhythm inversion, and review historical circadian activity reports. The outputs are behavioral rhythm analysis and care-environment prompts, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure footage or video URLs may be sent to a remote service for analysis.

Mitigation: Use only footage appropriate for remote processing, avoid sensitive or unrelated video, and confirm the configured service endpoint before running analysis.

Risk: Reports are linked to an automatically resolved local identity and service tokens may be stored in a workspace SQLite database.

Mitigation: Review local workspace data access, confirm the identity behavior is acceptable, and remove or rotate stored tokens when the workspace is shared or retired.

Risk: Endpoint scope and retention or deletion behavior are not clearly documented in the evidence.

Mitigation: Verify production endpoints and retention/deletion expectations before deployment, especially for continuous 24-hour or multi-day video workflows.

Risk: Circadian analysis can be mistaken for veterinary diagnosis or precise environmental control instructions.

Mitigation: Treat outputs as behavior-analysis guidance only, avoid specific drug or dosing advice, avoid unconfirmed lighting-control actions, and consult a reptile veterinarian when health signs persist.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files]

**Output Format:** [Markdown text containing structured JSON-style analysis, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include fields such as report date, enclosure and individual IDs, species rhythm label, hourly activity array, peak hours, rhythm consistency score, alert level, recommended actions, and disclaimer.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes fixed-camera overnight footage for a person living alone to compare lights-off time and early-morning activity against a personal baseline and produce a non-diagnostic rhythm anomaly reminder.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers, community workers, and remote-care operators use this skill to review overnight home video for sleep-rhythm deviations in people living alone and to generate structured reports or check-in reminders. It reports visual rhythm parameters and deviations, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private overnight home video or camera URLs may be uploaded to cloud analysis services.

Mitigation: Use only with clear consent from the monitored person or legal guardian, remove credentials and sensitive query tokens from URLs, and limit input to the minimum video needed for the analysis.

Risk: Reports may be associated with an automatically resolved identity and retrieved from cloud history.

Mitigation: Confirm that the active workspace identity and report recipients are authorized before analysis or history lookup.

Risk: Sleep-rhythm deviations can be mistaken for medical conclusions.

Mitigation: Present outputs as visual rhythm indicators and check-in prompts, and route health concerns to qualified caregivers or clinicians.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands]

**Output Format:** [Markdown summaries and JSON-style structured analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud query results; output should avoid medical diagnosis.]

## Skill Version(s):

1.0.7 (source: server release evidence; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

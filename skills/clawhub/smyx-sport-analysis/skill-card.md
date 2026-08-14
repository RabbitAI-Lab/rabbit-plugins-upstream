## Description:

Conducts video safety risk analysis for participants in outdoor sports competitions, long-distance running, marathons, etc.; identifies sports injuries and sudden health risks, outputs professional analysis reports, and provides timely warnings to support sports safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event operators, safety teams, and agents use this skill to submit outdoor sports video or video URLs for remote risk analysis, structured reports, safety warnings, and historical report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded sports footage, report history, and account-linked identifiers are processed by a remote LifeEmergence service.

Mitigation: Use only footage and report data that participants are authorized to share, and confirm remote retention, access, and deletion expectations before deployment.

Risk: The skill creates or reuses local identity records and stores returned authentication tokens locally.

Mitigation: Run in a controlled workspace, protect local files from unauthorized access, and clear persisted user records or tokens when the workspace is retired.

Risk: Analysis results may concern injuries or acute health risks but are not a substitute for professional medical judgment.

Mitigation: Treat outputs as safety support and route suspected emergencies or participant health concerns to qualified medical personnel.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Outdoor sports risk analysis API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown text with optional JSON details and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include structured risk findings, safety guidance, historical report tables, and report export links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

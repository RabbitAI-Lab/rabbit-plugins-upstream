## Description:

Analyzes fixed-camera reptile enclosure video to estimate hourly motion, compare observed activity against species circadian patterns, and produce rhythm reports with alerts and husbandry guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reptile keepers, husbandry operators, and research observers use this skill to analyze 24-hour or multi-day fixed-camera enclosure footage for activity distribution, rhythm alignment, and anomaly alerts. It supports report generation and cloud history lookup for enclosure and individual-level rhythm records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends enclosure footage, report metadata, and an internal account identifier to a third-party cloud service.

Mitigation: Use it only after confirming the data-sharing posture is acceptable, and avoid submitting sensitive footage unless the deployment has appropriate consent and retention controls.

Risk: The security evidence reports shipped development or plaintext HTTP configuration that may expose videos or credentials.

Mitigation: Configure a production HTTPS endpoint and review API key handling before processing real enclosure data.

Risk: The security evidence reports local token persistence that may make the workspace sensitive.

Mitigation: Restrict access to the local workspace, treat local databases and configuration as credential-bearing files, and rotate tokens if exposure is suspected.

Risk: Rhythm outputs could be mistaken for veterinary diagnosis or precise environmental control instructions.

Mitigation: Present results as motion-based rhythm analysis, preserve artifact constraints against medical diagnosis or medication guidance, and refer persistent abnormalities or health signs to a qualified reptile veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Reptile circadian activity API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown reports, JSON analysis payloads, shell commands, and optional saved text output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include hourly activity arrays, peak and quiet hours, rhythm classifications, alert levels, recommended actions, report links, and history tables.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact SKILL.md frontmatter is 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Match and prioritize job listings against a candidate profile using KSAO-based dual-layer funnel scoring with Agent reasoning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iichaner](https://clawhub.ai/user/iichaner)

### License/Terms of Use:

MIT-0

## Use Case:

External users and job seekers use this skill to compare resumes and preferences against job descriptions, calibrate matching rules, and prioritize roles as high, medium, or low fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can process sensitive resume content and job data.

Mitigation: Redact unnecessary personal details where possible and confirm what resume, job description, Feishu table, or local file will be read before running the workflow.

Risk: The workflow can update Feishu tables or create result files with match judgments.

Mitigation: Ask for a dry run or explicit confirmation before writing results back to shared tables, and verify target table fields and record identifiers before batch updates.

Risk: Incomplete job descriptions, missing salary or location data, and uncalibrated thresholds can lead to inaccurate priorities.

Mitigation: Use the calibration step with at least 10 representative job descriptions, flag incomplete records, and treat generated priorities as decision support rather than final hiring or application decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/iichaner/job-match-priority)
- [ClawHub skill page](https://clawhub.ai/iichaner/skills/job-match-priority)
- [Candidate Profile Reference](references/candidate-profile.md)
- [Priority Rules Reference](references/priority-rules.md)
- [Field Configuration Reference](references/field-config.md)
- [Usage Guide](assets/usage-guide.md)
- [Edge Cases](assets/edge-cases.md)

## Skill Output:

**Output Type(s):** [analysis, markdown, configuration, guidance]

**Output Format:** [Markdown analysis with priority labels, concise reasons, matched dimensions, depth-match notes, and optional CSV, Excel, or Feishu table updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces high, medium, or low job-match priorities after user-confirmed calibration; local file outputs are written as new result files rather than modifying originals.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

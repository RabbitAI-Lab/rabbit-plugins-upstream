## Description:

Analyzes litter-box area video or image inputs to estimate individual cat entry and exit events, daily usage frequency, per-visit duration, historical-baseline changes, and behavior-statistics-based urinary health alerts without providing a medical diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators in multi-cat homes, catteries, veterinary inpatient wards, or boarding centers use this skill to analyze litter-box footage, produce structured usage reports, and surface behavior-statistics-based urinary health alerts for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Litter-box videos or URLs may be sent to a remote service.

Mitigation: Use only media that is appropriate for remote processing, and avoid private home footage, signed URLs, or internal URLs unless the deployment has explicit approval for that data flow.

Risk: The skill may create or reuse an account identity and store tokens locally in the workspace.

Mitigation: Install only in environments where local token storage is acceptable, and review workspace storage, retention, and access controls before use.

Risk: Cloud report history may be queried automatically with limited user-facing control.

Mitigation: Confirm that report-history access matches user expectations and organizational policy before enabling historical report workflows.

Risk: Behavior-statistics alerts may be mistaken for medical diagnosis.

Mitigation: Present outputs as screening or monitoring signals only, and direct users to veterinary review for diagnosis or treatment decisions.

## Reference(s):

- [API Documentation](artifact/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud report history and produce behavior-statistics-based alerts; does not provide medical diagnosis.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

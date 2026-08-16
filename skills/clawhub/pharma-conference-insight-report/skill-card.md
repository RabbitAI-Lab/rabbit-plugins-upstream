## Description:

Generates a strategic pharma conference insight report by researching recent AACR, ASCO, and CSCO data for a target company and producing an HTML report covering technology trends, tumor landscapes, target competition, competitors, BD signals, actions, and risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Pharma strategy teams, executives, and investment decision makers use this skill to generate oncology conference intelligence for a target company, including recent AACR/ASCO/CSCO findings, competitor analysis, BD signals, recommended actions, and risk monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: External research can retrieve stale, incomplete, or inaccurate conference and competitor information.

Mitigation: Review cited sources and key conclusions before using the report for strategic or investment decisions.

Risk: The skill writes an HTML report to a user-selected output path.

Mitigation: Keep output_path inside a session or project folder and avoid paths that could overwrite important files.

Risk: Generated reports may load Chart.js from an external CDN when opened.

Mitigation: Open the report only in environments where external CDN access is acceptable, or replace the dependency with an approved local copy before sharing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Code, Files, Guidance]

**Output Format:** [Single-file HTML report with embedded CSS, JavaScript, Chart.js visualizations, and source notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May load Chart.js from an external CDN when opened; default output path is @session/{company}_report.html.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

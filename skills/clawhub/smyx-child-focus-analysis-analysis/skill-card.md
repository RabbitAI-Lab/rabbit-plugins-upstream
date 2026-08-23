## Description:

Analyzes child study-area images or videos from a smart desk lamp or tabletop camera to estimate focus scores, identify distraction periods, and generate structured reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, teachers, and developers integrating study-lamp, home-study, or classroom monitoring workflows use this skill to submit child study-area media and receive focus scores, distraction-event statistics, historical report links, and alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's study-area videos or video URLs are sent to the configured lifeemergence.com backend.

Mitigation: Use only with guardian consent and after confirming the backend's privacy, retention, deletion, and access-control terms for child footage.

Risk: Results are linked to an automatically managed account identity and can include historical report access.

Mitigation: Confirm who can access historical reports and avoid using real child footage until account association and report visibility are understood.

Risk: Backend authentication tokens may be stored in the workspace data directory.

Mitigation: Run the skill only in a trusted workspace and protect or clear stored tokens according to local security policy after use.

## Reference(s):

- [Child Focus Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON report text with optional report links and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include focus scores, distraction-event tables, alerts, historical report listings, and cloud report links.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

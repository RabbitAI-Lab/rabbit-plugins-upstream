## Description:

Analyzes pet images, videos, or URLs through remote services to produce 3D body-shape observations and a Body Condition Score (BCS 1-9) for weight-management reference, without diagnosing disease or prescribing treatment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill in pet health management, smart feeder, and pet camera workflows to evaluate body condition from multi-angle pet media and retrieve prior analysis reports. Results are intended as weight-management observations and should be reviewed alongside veterinary judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, supplied URLs, and identity data are sent to lifeemergence.com services for analysis and history retrieval.

Mitigation: Use only with media that the user is authorized to share, and review the remote service's retention, account, and privacy controls before deployment.

Risk: The skill can silently create or reuse an internal account identity and query cloud history tied to that identity.

Mitigation: Run in a controlled workspace with explicit operator awareness of account linkage, and avoid using shared workspaces for unrelated users.

Risk: Reusable authentication tokens may be stored in a local workspace database.

Mitigation: Protect workspace storage, restrict filesystem access, and rotate or clear stored credentials when decommissioning or transferring the workspace.

Risk: BCS output is a visual estimate and is not a veterinary diagnosis or treatment plan.

Mitigation: Present results as weight-management reference information and recommend veterinary review for health decisions.

## Reference(s):

- [Pet Health Analysis API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like text containing structured body-condition observations, risk prompts, suggestions, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write analysis output to a user-specified file path; history queries are formatted from cloud API results.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

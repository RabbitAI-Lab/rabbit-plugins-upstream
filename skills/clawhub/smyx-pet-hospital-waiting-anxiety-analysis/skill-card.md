## Description:

Analyzes pet hospital waiting-area video files or URLs through server-side APIs to identify anxiety-related behavior signals and return a structured 1-5 anxiety level for veterinary workflow support without diagnosis or treatment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Veterinary clinic staff and pet-care operators use this skill to analyze waiting-area pet videos for visible stress signals and prioritize comfort or care workflows. The output is workflow support only and does not provide disease diagnosis or treatment plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Clinic pet videos or supplied URLs may be sent to configured lifeemergence.com services for analysis.

Mitigation: Use only footage that the clinic is authorized to process with the remote service, and confirm consent, retention, and data handling terms before using real clinic videos.

Risk: The skill can silently create or reuse an identity and associate reports with that identity.

Mitigation: Require an explicit consent or authentication flow before deployment, and document which identity is used for report association.

Risk: Reusable service tokens may be stored in the workspace data directory.

Mitigation: Restrict workspace access, rotate or revoke tokens when no longer needed, and avoid sharing workspaces that contain token state.

Risk: Historical report queries can retrieve cloud report history.

Mitigation: Limit access to trusted operators and review report-history permissions before enabling the skill in shared environments.

## Reference(s):

- [Pet Health Analysis API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Structured text or JSON report, with Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include anxiety level, observed behavior signals, recommendations, report links, and historical report listings.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

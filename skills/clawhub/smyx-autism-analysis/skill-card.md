## Description:

Performs special video analysis on behavioral characteristics of children with autism, identifies core symptom features, provides structured analysis reports and intervention recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, caregivers, educators, and professionals can use this skill to submit child behavior videos or video URLs for preliminary autism-spectrum behavior analysis, structured report generation, and intervention-oriented guidance. It also supports querying prior analysis reports associated with the locally managed user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends sensitive children's videos or video URLs to a configured remote backend for analysis.

Mitigation: Use only with appropriate consent and after verifying the service endpoint, privacy policy, retention process, deletion process, and suitability for real children's media.

Risk: The skill creates or reuses a local identity and may store tokens in the workspace.

Mitigation: Review local workspace storage before and after use, restrict workspace access, and remove identities or tokens that should not persist.

Risk: Autism-spectrum analysis output can be mistaken for a clinical diagnosis.

Mitigation: Treat results as preliminary screening guidance only and refer suspected cases to qualified medical or developmental professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or JSON text containing structured analysis results, recommendations, history-report tables, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include risk or recognition findings, suggested next steps, and links to generated reports.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

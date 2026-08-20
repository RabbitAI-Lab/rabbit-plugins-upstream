## Description:

Analyzes multi-angle pet videos or URLs through a remote service to reconstruct body shape, estimate a 1-9 Body Condition Score, classify body type, and return structured body-condition observations without disease diagnosis or treatment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and pet health platform operators use this skill to submit pet media for BCS-oriented body-shape analysis and to retrieve structured analysis reports for weight-management workflows. Results are for body-condition observation and should not be treated as veterinary diagnosis or treatment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media, URLs, and historical report requests may be sent to remote backend services.

Mitigation: Confirm backend endpoints, account model, retention rules, and user consent before deployment.

Risk: The skill may silently create or reuse a local identity, store tokens, and query historical reports under that identity.

Mitigation: Use per-user workspace isolation, avoid shared workspaces unless isolation is guaranteed, and review credential storage and report-access controls before installation.

Risk: BCS results are visual estimates and may be misleading if treated as medical conclusions.

Mitigation: Present results as body-condition observations for weight-management support and direct users to veterinary review for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented structured reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include BCS score, body-type classification, observations, risk prompts, suggestions, and historical report links returned by the remote service.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

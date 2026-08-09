## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts for home pet monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Home pet owners and agents use this skill to analyze pet-monitoring videos or URLs for restricted-area intrusion, table climbing, and trash rummaging. It returns structured alerts, report text, and report links for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-monitoring videos or URLs may be processed by the publisher's cloud service.

Mitigation: Use the skill only where sharing household media with the publisher's cloud service is acceptable, and review retention and deletion controls before deployment.

Risk: The skill can create or reuse a local and remote-linked identity for report history.

Mitigation: Review token and report-history storage, and add deployment controls if history queries should require explicit user confirmation.

Risk: The security evidence reports limited user-facing control over report history and token handling.

Mitigation: Restrict network use and history retrieval to trusted environments, and document operational controls for users who manage household media.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown reports and JSON structured analysis, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and history lists associated with the resolved user identity.]

## Skill Version(s):

1.0.10 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

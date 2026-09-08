## Description:

This skill analyzes fixed-camera video of an elderly person's water-cup area to count cup pickup events and report non-diagnostic dehydration-risk indicators for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers, family members, nursing-home staff, and home-care platform operators use this skill to review camera footage for water-cup pickup frequency, long gaps without detected cup use, and trend-based reminders. The output is a visual behavior summary and directional alert, not a medical diagnosis or direct measurement of water intake.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends elderly-care camera footage and report requests to a configured service.

Mitigation: Use the skill only with informed consent from the monitored person or guardian, and confirm the service endpoint, retention expectations, and access controls before deployment.

Risk: The security review reports persisted identity credentials and a local SQLite user/token database.

Mitigation: Review where the local database is stored, restrict file access, and rotate or remove credentials used during testing or installation.

Risk: The security review flags insecure default network settings and shipped development HTTP endpoints.

Mitigation: Require production HTTPS endpoints before real use and remove or override development endpoint configuration.

Risk: Cup pickup counts are only an indirect proxy for drinking and can be wrong when the cup is empty, handled by someone else, or outside the camera's stable view.

Mitigation: Treat alerts as prompts for caregiver follow-up and combine them with drinking gestures, personal baselines, and direct welfare checks.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Analysis API error-code reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown text with structured JSON-style analysis, risk labels, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the same textual result to a user-specified output file.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

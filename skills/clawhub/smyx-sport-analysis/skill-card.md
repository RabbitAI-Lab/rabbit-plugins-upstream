## Description:

Conducts video safety risk analysis for participants in outdoor sports competitions, long-distance running, marathons, etc.; identifies sports injuries and sudden health risks, outputs professional analysis reports, and provides timely warnings to ensure sports safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event operators, medical response teams, and agents supporting outdoor sports events use this skill to submit participant video or image evidence for risk analysis, retrieve structured reports, and query prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive participant and health-adjacent sports videos through remote services.

Mitigation: Use real participant media only after reviewing service and data-retention terms and obtaining appropriate consent.

Risk: Security evidence flags remote service use, identity linkage, and locally reusable tokens as review concerns.

Mitigation: Require scoped history access, protected token storage, and reviewer approval before operational deployment.

Risk: Artifact configuration includes non-HTTPS and test or private endpoints.

Mitigation: Configure HTTPS-only production endpoints and prevent test or private endpoints from being used in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown-style text and JSON analysis results with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a user-specified file path.]

## Skill Version(s):

1.0.13 (source: ClawHub release evidence; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes camera footage from public venues to estimate aggregate facial-expression distributions and a group emotion index, then provides operational suggestions and safety cues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Venue operators can use aggregate emotion reports from fixed-camera footage to understand visitor experience and guide service or layout changes. Safety cues are supplementary and require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends camera footage to a cloud service, and the processor's privacy and retention practices are unverified.

Mitigation: Require explicit emotion-analysis intent and approve the cloud processor and its retention terms before use with footage.

Risk: The security review flags possible API secret exposure, automatic account registration, and analysis running despite the setup-only option.

Mitigation: Wait for fixes to secret handling and the setup-only option before using real credentials or camera footage, and isolate the local account database.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports with emotion distributions, group and regional indices, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Aggregated group-level estimates; small samples may be marked insufficient for an index.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

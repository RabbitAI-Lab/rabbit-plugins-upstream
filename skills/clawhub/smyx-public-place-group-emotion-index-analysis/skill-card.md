## Description:

Analyzes public-venue camera videos to summarize group facial-expression distributions and a group-emotion index, with operational suggestions and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Venue operators and their developers use the skill to review aggregate emotion indicators from public-space videos and access historical reports for service planning and human-reviewed safety awareness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-camera footage or video URLs are sent to an external service.

Mitigation: Use only authorized footage; provide appropriate venue notice and review consent, retention, and access controls before use.

Risk: The skill can create or reuse a cloud-linked identity and store a local token, affecting access to reports.

Mitigation: Review report ownership and local token access; do not disclose internal identity values.

Risk: Group-emotion scores can be over-interpreted as evidence about individuals or safety.

Mitigation: Require human review before interventions and avoid individual profiling or discriminatory use.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown table of historical reports; JSON output is supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes aggregate emotion indicators, recommendations, and report links when available.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

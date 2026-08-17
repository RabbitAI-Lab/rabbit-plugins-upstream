## Description:

Using fixed cameras in malls, exhibition halls, scenic areas and other public places, the system analyzes facial expressions of multiple people in the scene in real time with anonymized expression recognition, aggregates emotion distribution, and computes an overall group-emotion index from 0 to 100.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, venue teams, and developers use this skill to analyze public-place video or image inputs for anonymous group-level emotion distribution, regional emotion indexes, operational suggestions, and safety-warning guidance. It is intended for malls, exhibitions, scenic areas, airports, museums, and similar public venues where aggregate customer or crowd sentiment can inform staffing, layout, and monitoring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-place video, video URLs, derived reports, workspace-linked identity values, and authentication metadata may be sent to external LifeEmergence services.

Mitigation: Deploy only after confirming data-sharing approvals, public notice, retention limits, and contractual controls for the configured external services.

Risk: Persistent local report, account, identity, or token state may conflict with user expectations created by anonymous-analysis wording.

Mitigation: Review local state handling before installation, restrict access to generated state files, and document what identifiers or tokens are retained.

Risk: Group emotion outputs can be misused for individual decisions or automated interventions.

Mitigation: Use outputs only as aggregate operational guidance, keep human review in the loop, and prohibit identity matching, tracking, discrimination, or individual-level service changes.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style analysis reports with metrics, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include group emotion distribution, index values, region breakdowns, warning levels, operational suggestions, safety suggestions, and optional saved report files.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

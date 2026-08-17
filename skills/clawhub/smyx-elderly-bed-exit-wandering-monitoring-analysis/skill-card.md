## Description:

Identifies abnormal behaviors such as getting out of bed at night, prolonged wandering, and remaining motionless for extended periods for nighttime elder-care monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care operators, and developers use this skill to analyze night monitoring videos or URLs for bed-exit, wandering, and extended immobility signals, then review structured reports and cloud report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elder-care video, provided URLs, and report queries are sent to external cloud services.

Mitigation: Use the skill only when cloud processing and account linkage are acceptable for the footage and reports involved.

Risk: The skill may silently create or reuse a local and remote account identity with stored tokens.

Mitigation: Review account identity and token storage behavior before installation, and remove stored identifiers when they are no longer needed.

Risk: Monitoring output may be mistaken for a definitive safety or medical determination.

Mitigation: Treat alerts and reports as caregiver decision support and confirm abnormal events with human review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-bed-exit-wandering-monitoring-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis, with optional output file content and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud report history and return export links; accepted media inputs are local files or public URLs.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes outdoor images and videos to detect people, vehicles, non-motorized vehicles, and pets, and produces monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users can analyze outdoor surveillance images and videos to identify people, vehicles, non-motorized vehicles, and pets, review monitoring results, and query reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option can still upload footage to the remote service.

Mitigation: Avoid private footage until this behavior is fixed; use non-sensitive test media and confirm the service's upload and retention practices.

Risk: Account handling can expose credentials.

Mitigation: Keep API secrets out of identity fields and URLs, and protect the shared token database.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [API interface documentation](references/api_doc.md)
- [API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown reports, Report links]

**Output Format:** [Structured analysis results in JSON and Markdown summaries or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include detected targets, risk assessments, recommendations, and links.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

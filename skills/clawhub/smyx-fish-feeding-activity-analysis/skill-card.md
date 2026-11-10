## Description:

Analyzes post-feeding fish videos to estimate feeding activity, remaining feed, and possible appetite changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and developers can use the skill to review fish feeding videos, track feeding activity, and receive visual observations and follow-up suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account and token handling, remote service activity, and incomplete inspection.

Mitigation: Clarify why account and token management is needed, which service receives video and identity data, and resolve the missing referenced path before use.

Risk: The security review reports that export-only mode may still trigger analysis.

Mitigation: Verify the export-only behavior before relying on it to avoid analysis or data transfer.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill introduction video](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON feeding report; Markdown table for history listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a feeding activity score, observations, alert level, suggested actions, and a report link when available.]

## Skill Version(s):

1.0.19 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

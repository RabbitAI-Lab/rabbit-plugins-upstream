## Description:

Identifies individual livestock (pigs, cattle, sheep) by facial or body-pattern features and outputs a stable individual ID with confidence for precision farm management and tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, livestock management teams, and developers use this skill to identify pigs, cattle, and sheep from images, videos, or URLs and receive a structured report with individual IDs, confidence, matched visual features, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm images, videos, URLs, and identity data may be sent to external analysis services.

Mitigation: Install only after verifying the configured API endpoints and confirming that uploaded media is appropriate for the service and publisher.

Risk: The skill can create or reuse a local identity and store tokens in a workspace SQLite database.

Mitigation: Use a dedicated workspace, review local identity and token storage expectations before use, and avoid sharing the workspace with untrusted users.

Risk: Historical cloud report queries can expose prior report metadata for the resolved identity.

Mitigation: Run history queries only when report tracking for the current identity is intended and acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-individual-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Livestock Individual Identification API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Markdown or JSON structured livestock identification report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include individual IDs, confidence scores, matched feature areas, historical report entries, export links, and optional saved output files.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; artifact frontmatter says 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

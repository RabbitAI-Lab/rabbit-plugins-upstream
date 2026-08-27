## Description:

Analyzes fish fry tank images or videos with a known-size reference object to estimate body length, growth rate, growth curves, and growth-related alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquaculturists, ornamental fish breeders, laboratory users, and developers use this skill to analyze periodic fry tank media, measure fry length in millimeters, compare growth over time, and generate structured growth reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send fish-tank media and report queries to external cloud or private API services.

Mitigation: Install only when the publisher and configured API endpoints are trusted, and avoid submitting media that should not leave the workspace.

Risk: The skill can automatically create or reuse an identity, read workspace credentials, and persist returned tokens locally.

Mitigation: Review credential handling before use, run in an isolated workspace when possible, and remove local credentials or token databases when no longer needed.

Risk: Measurements can be misleading when the reference object is missing, off-plane, low confidence, or captured from a non-vertical perspective.

Mitigation: Use a known-size reference object in the same plane as the fish, capture from directly overhead, and treat low-confidence or obstructed results as requiring a new image or video.

## Reference(s):

- [API Interface Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured analysis, growth measurements, report links, historical report tables, and optional saved output files.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

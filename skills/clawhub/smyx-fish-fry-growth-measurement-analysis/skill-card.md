## Description:

Through fixed cameras of fry tanks, this skill analyzes images or videos with a known-size reference object to measure fry body length, estimate growth rate, plot growth curves, and report measurement reliability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculture operators, ornamental fish breeders, laboratory staff, and agent developers use this skill to analyze fry tank media, convert pixel measurements into millimeters using a reference object, review growth trends, and retrieve account-linked historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected local media or URLs to Life Emergence cloud services for analysis.

Mitigation: Use only media that the user is authorized to upload, avoid sensitive scenes, and confirm that cloud processing is acceptable before deployment.

Risk: The skill can silently create or reuse an internal account identity and query account-linked history.

Mitigation: Deploy only where account identity handling, history access, retention, and deletion controls have been reviewed and documented.

Risk: Service tokens may be stored in a local workspace SQLite database.

Mitigation: Restrict workspace access, rotate tokens when needed, and prefer a release that makes token storage and cleanup behavior explicit.

Risk: Image quality, missing reference objects, perspective distortion, or bent fish posture can make body-length and growth estimates unreliable.

Mitigation: Require clear top-down media with a same-plane reference object and treat low-confidence or obstructed inputs as measurement-unreliable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON reports with measurement statistics, growth curves, alert levels, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires clear fry tank media with a same-plane reference object; unreliable images should return a measurement-unreliable result rather than growth conclusions.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes seedling tray images or videos with AI object detection to identify emerged seedlings, count germinated seeds, estimate germination rate, and retrieve historical analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users such as greenhouse nursery operators, home planting users, and seed-company test staff use this skill to analyze seedling tray images or videos for visual germination counts, germination-rate estimates, low-rate alerts, and report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review states that the skill may upload images or videos to a backend service and query cloud history.

Mitigation: Review backend service trust, data handling, and user consent requirements before installation or execution.

Risk: The security review states that the skill automatically associates activity with an internal identity and keeps reusable tokens in a local SQLite database.

Mitigation: Use only in environments where this identity handling is acceptable, and inspect local token storage before production use.

Risk: The security review states that shipped default configuration points to plaintext private-network HTTP endpoints.

Mitigation: Replace plaintext or private-network defaults with reviewed HTTPS service endpoints before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-seed-germination-rate-prediction-analysis)
- [Seed germination API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, Markdown history tables, or JSON-style structured text from CLI/API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis output to a user-specified file and may include report links for historical records.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Triggers when a user provides images or videos of crop leaves, buds or fruits for pest identification, calls server-side APIs to detect common agricultural pests, and outputs pest types with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze crop leaf, bud, or fruit images and videos for common pest identification, quantity estimates, confidence scores, and report links. The skill is intended to support early pest observation and farm decision workflows, not to prescribe pesticide treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop media or media URLs are sent to a cloud-backed analysis service.

Mitigation: Use only with media that the user is permitted to upload, avoid unrelated sensitive content, and run the skill in an environment with reviewed network access.

Risk: The skill can create or reuse a local identity and store authentication tokens in a workspace SQLite database.

Mitigation: Review the local data directory before installation, protect or clear stored credentials between users, and prefer an isolated workspace for evaluation.

Risk: The skill can retrieve prior analysis reports tied to the local identity.

Mitigation: Confirm history lookup is expected before using report-list features and restrict access to workspaces that may contain another user's report history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Crop pest API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON pest analysis report with confidence scores and report links; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated from server-side analysis of a local media upload or remote media URL and may include cloud report history for the current local identity.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

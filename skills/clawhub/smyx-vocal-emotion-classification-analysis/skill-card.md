## Description:

Analyzes dog or cat vocalization audio/video inputs, extracts acoustic features, and returns emotion classifications with confidence scores without providing medical, training, or behavior-modification advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to classify pet vocal emotion from uploaded or URL-based audio/video, review confidence-scored results, and retrieve cloud-hosted historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet audio/video and related metadata may be uploaded to the publisher's remote service.

Mitigation: Use only media that is approved for remote processing and avoid sensitive household, location, or account-identifying content.

Risk: The skill may create or reuse an internal user, read workspace identity material, and store tokens locally.

Mitigation: Review identity and token handling before installation, run in a restricted workspace, and remove local tokens when the skill is no longer needed.

Risk: Historical cloud report links may expose prior reports tied to the resolved identity.

Mitigation: Confirm that report-history access is expected for the user and restrict use to authorized identities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vocal-emotion-classification-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Markdown or JSON analysis report with confidence scores and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and historical report tables when list mode is used.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes meal images and videos to identify dietary behavior patterns, generate structured health reports, and provide nutrition improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit meal media or media URLs for dietary behavior analysis, review structured reports, and retrieve historical analysis reports from the remote service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive meal media or URLs may be uploaded to a remote service for analysis.

Mitigation: Review the configured endpoints and data handling before use, and avoid private health-related media unless the service is approved for that data.

Risk: The skill may create or reuse an internal identity and store local account tokens.

Mitigation: Run the skill in an isolated account or workspace, protect local token files, and clear stored credentials when analysis is complete.

Risk: Default development HTTP endpoints conflict with the skill's HTTPS-only privacy claim.

Mitigation: Require production HTTPS endpoints or a documented explanation before using the skill with private media.

Risk: Dietary analysis reports and nutrition recommendations can be mistaken for professional medical advice.

Mitigation: Present outputs as informational guidance and direct users with health concerns to qualified nutrition or medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Diet analysis API documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown text or JSON structured reports, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; local media inputs are limited to mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

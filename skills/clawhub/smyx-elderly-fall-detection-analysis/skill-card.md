## Description:

Detects potential elderly falls from monitoring images, videos, or URLs and returns structured analysis results, report links, and historical report listings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-monitoring developers use this skill to submit home monitoring media for elderly fall detection and to retrieve prior fall-analysis reports from the connected cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home monitoring images, videos, URLs, and report-history requests are sent to the Life Emergence/Smyx cloud service.

Mitigation: Use the skill only when the media-sharing, retention, account deletion, and report-access terms for that service are acceptable for the people being monitored.

Risk: The skill can silently create or reuse a local identity and store returned tokens in the workspace data directory.

Mitigation: Review the workspace data directory and account behavior before deployment, and restrict filesystem access to users who are allowed to access those credentials.

Risk: Fall-detection output may be incorrect or incomplete and is not a substitute for emergency confirmation.

Mitigation: Treat alerts as safety triage signals and verify suspected falls through direct contact or emergency response procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-fall-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Smyx analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis output can include structured fall-detection results, historical report listings, and export URLs returned by the remote service.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

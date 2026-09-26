## Description:

Automatically detects electric motorcycles and e-bikes in restricted areas from videos or images, counts illegal parking or driving instances, and returns violation alerts and management suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, facility operators, and security teams use this skill to analyze surveillance video, images, or media URLs for e-bike violations in restricted areas such as parks, communities, campuses, parking areas, and roads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos, images, or media URLs may be sent to configured Lifeemergence cloud services for analysis.

Mitigation: Use only media approved for cloud processing, avoid sensitive surveillance footage unless authorized, and confirm retention and privacy terms before deployment.

Risk: The skill can silently create or reuse an account identity and store authentication tokens locally.

Mitigation: Run it in a controlled workspace, protect or clear local token storage according to policy, and approve the account model before shared use.

Risk: A hidden caller-controlled identity path and report-history access may expose reports outside the intended account boundary.

Mitigation: Restrict who can supply identity context, validate report-history access against the authorized account, and review generated report links before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [Electric vehicle detection API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON analysis reports, with optional saved text or JSON output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include violation counts, risk levels, management warnings, suggestions, report export links, and cloud report-history results.]

## Skill Version(s):

9.9.17 (source: server release metadata; artifact frontmatter reports 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

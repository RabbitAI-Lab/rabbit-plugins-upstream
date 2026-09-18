## Description:

Detects whether anyone has fallen within a specified target area from images or short videos, and returns structured analysis, risk signals, recommendations, and report links for home-care or nursing-home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregiving teams, family members, and developers use this skill to send existing monitoring images or short videos to a cloud fall-detection service and receive structured fall-risk results. It can also retrieve cloud-hosted historical analysis reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home-care images or videos are uploaded to a cloud service and may be retained with reports.

Mitigation: Use only with a trusted publisher and service, and only with media that users are authorized to share; review data retention and access expectations before deployment.

Risk: The skill silently creates or reuses an internal identity and stores returned tokens in a local workspace database.

Mitigation: Review identity and token handling before use in real caregiving settings, and limit workspace access to trusted operators.

Risk: Fall-detection output can be wrong or incomplete and is not a substitute for emergency confirmation.

Mitigation: Treat results as safety screening signals; confirm suspected falls through human follow-up and emergency procedures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-image-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with structured JSON snippets and optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output report export links and historical report lists; --output can save returned content to a file.]

## Skill Version(s):

1.0.14 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

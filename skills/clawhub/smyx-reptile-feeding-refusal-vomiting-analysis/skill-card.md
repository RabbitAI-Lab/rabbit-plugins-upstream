## Description:

Analyzes reptile enclosure feeding and post-feeding videos to identify prey attacks, successful swallowing, feeding refusal, and regurgitation events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, reptile keepers, vivarium operators, and developers use this skill to turn fixed-camera feeding videos into behavior records, alerts, and report links for refusal or vomiting review. The output is advisory behavior analysis and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure videos and report history may be sent to a remote analysis service.

Mitigation: Use the skill only with user consent and with footage that is appropriate for cloud processing.

Risk: The security review reports silent identity handling and persisted tokens.

Mitigation: Review account access flows and token storage before using the skill with private or sensitive footage.

Risk: The security review reports default unencrypted development API endpoints.

Mitigation: Require HTTPS production endpoints before deployment.

Risk: Feeding refusal or vomiting classifications could be mistaken for a veterinary diagnosis.

Mitigation: Present results as visual behavior records and direct users to a qualified reptile veterinarian for medical interpretation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON analysis reports with event metrics, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return current analysis results or a historical report table; reports may reference remote analysis results.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

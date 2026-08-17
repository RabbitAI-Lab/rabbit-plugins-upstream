## Description:

Combines TCM facial feature recognition with physiological indicator information to provide early warnings of high-risk stroke conditions such as cerebral infarction and cerebral hemorrhage, and provides lifestyle intervention suggestions and medical guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to screen stroke risk from face images or video plus optional physiological indicators, then receive a structured report with risk level, warning signals, intervention suggestions, medical guidance, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive face, video, and health information and sends it to external services.

Mitigation: Install only in environments where users have consented to this processing and where the publisher and backend service are trusted for health-data handling.

Risk: The skill can create or reuse a backend identity and store authentication tokens locally.

Mitigation: Review local token storage and workspace access controls before deployment, and remove stored credentials when the skill is no longer needed.

Risk: Historical report links can be fetched from the cloud when users trigger report-list phrases.

Mitigation: Restrict use to authorized users and confirm that cloud report access matches the intended user identity.

Risk: Stroke risk screening output could be mistaken for a medical diagnosis.

Mitigation: Present results as screening guidance only and direct high-risk users to professional medical evaluation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stroke-risk-screening-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API document](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON text with optional report links and saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis can include risk level, risk score, extracted facial features, health warnings, lifestyle suggestions, medical guidance, and historical report entries.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

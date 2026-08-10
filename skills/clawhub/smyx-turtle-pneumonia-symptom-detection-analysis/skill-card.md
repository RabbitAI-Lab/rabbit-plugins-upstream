## Description:

Analyzes fixed-camera turtle mouth and nasal video to flag visual pneumonia-risk signs such as unusually frequent open-mouth breathing, mucus, or nasal discharge in non-feeding contexts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and reptile-care operators use this skill to submit turtle enclosure video or URLs for cloud-backed visual screening, alert generation, and historical report lookup. It supports risk warnings and care guidance, not veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Turtle videos or URLs are sent to a configured cloud service for analysis.

Mitigation: Install and use only when cloud processing of the submitted media fits the user's privacy expectations.

Risk: The skill can silently create or reuse a local identity and retrieve cloud report history.

Mitigation: Review identity and history-access behavior before deployment, especially in shared workspaces.

Risk: Service tokens may be stored in the workspace data database.

Mitigation: Protect the workspace data store and rotate or revoke tokens if the workspace is shared or exposed.

Risk: Visual screening output could be mistaken for a veterinary diagnosis.

Mitigation: Present results as risk warnings only and direct users to a professional reptile veterinarian for diagnosis and treatment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and JSON from cloud-backed analysis or history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write an optional output file when requested.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

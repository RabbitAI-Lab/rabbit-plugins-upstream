## Description:

Identifies enrolled acquaintances in images or videos by comparing faces against a user-managed face database and returning recognized identities, locations, reports, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to analyze authorized home or office images and videos for known-person recognition after faces have been enrolled in a database. It can also retrieve cloud-hosted historical recognition reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes face images or videos and may upload local media to lifeemergence.com cloud services.

Mitigation: Use only with media that the operator is authorized to process, and review organizational privacy requirements before installation or execution.

Risk: The skill silently creates or reuses a user identity and fetches report history from the cloud.

Mitigation: Run it only in workspaces where the account context and cloud report access are appropriate for the intended user.

Risk: A local shared database may retain identity and token records.

Mitigation: Review workspace storage controls and clear or protect retained account data according to local policy.

## Reference(s):

- [Skill Demo](https://lifeemergence.com/sample.html)
- [Familiar Person Recognition API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Error Codes](artifact/skills/smyx_analysis/references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration]

**Output Format:** [Markdown and JSON-style structured analysis text with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include recognized identities, locations, analysis status, recommendations, and cloud report links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

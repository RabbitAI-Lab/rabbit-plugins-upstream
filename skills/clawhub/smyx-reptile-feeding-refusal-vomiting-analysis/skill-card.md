## Description:

Analyzes reptile feeding videos to identify prey attacks, swallowing, feeding refusal, and regurgitation and provide alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure operators use feeding videos or video URLs to review feeding refusal and regurgitation alerts, examine analysis reports, and retrieve report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or supplied URLs are sent to an external cloud service, potentially exposing private household footage.

Mitigation: Obtain consent and confirm the service's retention and account controls before submitting sensitive footage or URLs.

Risk: Cloud report history is associated with an automatically managed identity, and reusable service tokens are stored in a local SQLite database.

Mitigation: Review installation and access controls, protect the local database, and use only if the account and retention behavior is acceptable.

Risk: Poor camera coverage or missing feeding context may make refusal and vomiting alerts unreliable.

Mitigation: Check footage quality and species-specific feeding context; seek a reptile veterinarian for health concerns rather than treating alerts as a diagnosis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or Markdown history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes feeding events, alerts, suggested actions, and report links when available.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

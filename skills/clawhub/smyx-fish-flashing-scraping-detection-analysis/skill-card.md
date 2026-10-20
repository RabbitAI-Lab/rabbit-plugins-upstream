## Description:

Analyzes aquarium camera video for repeated fish flashing and scraping and reports possible ectoparasite risk without diagnosing a specific disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and aquaculture staff use the skill to analyze tank video or retrieve past reports, review unusual rubbing behavior, and decide whether to seek veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish video or video URLs are sent to a cloud service for analysis.

Mitigation: Obtain consent before submitting footage or URLs and confirm acceptable data retention before use.

Risk: The skill silently creates or reuses an identity and logs in to the cloud service.

Mitigation: Disclose account association to users and require approval before cloud analysis or history lookups.

Risk: Reusable service tokens are stored in the workspace data directory.

Mitigation: Limit workspace access and prefer a version that stores tokens through a safer secret mechanism.

Risk: Behavioral alerts could be mistaken for a parasite diagnosis or treatment advice.

Mitigation: Treat results as warnings only; refer suspected cases to a qualified aquatic veterinarian for examination.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Reports]

**Output Format:** [JSON or Markdown report with risk alerts and historical report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include rubbing frequency, duration, affected fish count, and suggested next steps; results do not establish a diagnosis.]

## Skill Version(s):

1.0.14 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

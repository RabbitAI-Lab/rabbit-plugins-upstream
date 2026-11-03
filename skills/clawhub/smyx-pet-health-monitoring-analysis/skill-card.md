## Description:

Analyzes pet photos and monitoring videos for behavior patterns such as eating, drinking, elimination, vomiting, and limping, then produces health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to review camera or feeder photos and videos, monitor everyday behavior, and access health monitoring reports. The reports are for reference and do not replace veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected household footage is sent to Life Emergence cloud processing, which may expose private information.

Mitigation: Review the service's privacy and pricing terms, and submit only footage you are comfortable uploading.

Risk: The security review found inadequate safeguards for account credentials.

Mitigation: Before installing, confirm credentials are restricted to approved HTTPS services and that account storage and deletion controls are clear.

Risk: The security review says export-only mode still permits analysis.

Mitigation: Verify export-only behavior before use and confirm whether submitted footage will still be analyzed.

Risk: Health monitoring results may be mistaken for a veterinary diagnosis.

Mitigation: Treat results as reference information and consult a veterinarian about abnormalities.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [Structured health monitoring results and reports, with Markdown report listings, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include behavior observations, health notices, and recommendations.]

## Skill Version(s):

1.0.18 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

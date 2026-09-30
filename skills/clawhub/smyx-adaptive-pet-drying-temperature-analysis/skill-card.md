## Description:

Analyzes pet images or videos to estimate breed or body type and fur density, then recommends a drying temperature and duration curve for grooming.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and developers of pet-drying devices can use full-body pet images or videos to request personalized drying temperatures and durations and review past reports. Recommendations are for grooming, not medical care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos and report history are processed by external services, and cloud history may be retrieved without clear consent.

Mitigation: Notify users and obtain their approval before uploads or history queries; provide controls for access, retention, and deletion.

Risk: The skill can silently create or reuse an identity and store authorization tokens in a local database.

Mitigation: Disclose account creation, require user control, and restrict access to locally stored credentials.

Risk: Drying recommendations could cause discomfort or burns if used without checking the pet and equipment.

Mitigation: Treat the curve as grooming guidance, monitor the pet and equipment, and adjust or stop drying if discomfort occurs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis)
- [Pet drying analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report or JSON result; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include temperature (°C), duration (minutes), care guidance, and a report link.]

## Skill Version(s):

1.0.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

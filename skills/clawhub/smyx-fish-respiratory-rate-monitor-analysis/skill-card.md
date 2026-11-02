## Description:

Analyzes aquarium video to estimate fish gill movement and respiratory rate, then reports abnormal patterns and suggested checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists, aquarium operators, and fish-care developers can use fixed-camera footage to review fish gill movement, respiratory-rate estimates, and abnormal-pattern alerts. The results support follow-up checks of water conditions and are not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may upload video even when configuration-only mode is selected.

Mitigation: Use a corrected release that honors configuration-only mode, confirm the provider's video retention and charges, and avoid footage that shows private surroundings.

Risk: Account credentials and identity values may be handled insecurely, and cached tokens or alert recipients may be exposed.

Mitigation: Use a corrected release that separates credentials from identity values, protects cached tokens, and restricts alert recipients.

## Reference(s):

- [API and input guidance](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Report links]

**Output Format:** [Structured JSON analysis or history results with abnormal-pattern alerts, suggested checks, and report links; concise text summaries are also available.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include respiratory-rate estimates, signal reliability, context, and suggested actions. Alerts are advisory.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

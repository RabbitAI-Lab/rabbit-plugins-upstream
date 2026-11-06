## Description:

Measures fish fry body length from images or video using a known-size reference object, tracks growth rates, and produces growth reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculture operators, ornamental fish breeders, and researchers can use the skill to estimate fry length, review growth trends, and identify measurements that may need follow-up. Its reports support husbandry review and do not provide disease diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the export-only option can still upload footage.

Mitigation: Wait for this behavior to be corrected; before using the skill, confirm consent for footage uploads and verify retention and destination practices.

Risk: The security review says automatic account handling inadequately protects credentials.

Mitigation: Use an isolated workspace and service-specific credentials, and wait for credential handling to be corrected before use.

Risk: The remote service's measurement quality and privacy guarantees remain unverified.

Mitigation: Confirm privacy and retention practices and review measurements against known examples before relying on reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured growth report text, Markdown, or JSON, with measurements, growth summaries, alerts, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report contents depend on the supplied imagery or video and available history. Measurement reliability depends on image quality, reference-object placement, and camera angle.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes fish-fry images or video with a known-size reference object to estimate body length, track growth rates and curves, and report growth concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculture operators, ornamental fish breeders, and developers use the skill to analyze calibrated fry-tank media, review growth measurements and trends, and retrieve historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill automatically creates or reuses a backend identity and stores access tokens locally.

Mitigation: Review account linkage before installation and ask the publisher about token retention, deletion, and permission scope.

Risk: Fish-tank media and generated history records are sent to configured lifeemergence.com services for cloud processing.

Mitigation: Use only media and records approved for cloud processing; review the destination and data-handling terms before use.

## Reference(s):

- [Fish fry measurement API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table; optional saved text or JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include measurements, growth trends, alerts, recommendations, and report links.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

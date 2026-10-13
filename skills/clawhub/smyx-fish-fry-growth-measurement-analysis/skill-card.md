## Description:

Analyzes fish fry images or videos using a known-size reference object to estimate body length and growth rate and provide growth reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculture operators and ornamental fish breeders use the skill to track fry growth from calibrated tank imagery, review historical measurements, and identify potential growth problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create a remote identity and retain authentication tokens in a local user database.

Mitigation: Review account creation and token retention before installation, especially on shared or regulated systems.

Risk: Fish tank images, videos, and identity-linked report requests may be sent to configured LifeEmergence services.

Mitigation: Use only with authorized imagery and accounts after reviewing the service's privacy and data-handling terms.

Risk: Missing or poorly aligned reference objects can make fish-length measurements unreliable.

Mitigation: Keep the reference in the same plane as the fry and check image quality and reliability warnings before acting on alerts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown growth report with optional historical report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include body lengths, growth rates, growth curves, recommendations, and measurement-reliability warnings.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

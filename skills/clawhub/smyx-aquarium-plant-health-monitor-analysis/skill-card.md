## Description:

Analyzes aquarium plant images or videos for visible health issues and provides health assessments and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquascapers, and aquarium shops use camera images or videos to check aquatic plants for discoloration, damaged leaves, algae, and possible nutrient deficiencies, then review care suggestions or past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium images, videos, or media URLs are sent to lifeemergence.com services for analysis.

Mitigation: Review the service's data handling before use; do not submit private or sensitive media unless acceptable.

Risk: The skill silently creates or reuses an account identity, stores account tokens locally, and retrieves account-linked cloud report history.

Mitigation: Review account creation, token storage, and cloud history access before installing or running the skill.

Risk: Image-based symptoms can be ambiguous or distorted by glare, blur, and water conditions.

Mitigation: Use clear images, corroborate findings with water tests, and consult an aquarium expert before major water-quality changes.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [Aquarium plant analysis API documentation](artifact/references/api_doc.md)
- [Analysis API error codes](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Structured JSON or Markdown text; report links and Markdown tables for history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be saved to a file; visual assessments are advisory.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md declares 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

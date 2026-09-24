## Description:

Assesses ornamental fish images or videos for body-color saturation and brightness, compares HSV measurements against species-specific baselines, and returns a vibrancy score, trend information, and husbandry-oriented recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture staff, and app developers use this skill to analyze fish-side images or videos, monitor color vibrancy over time, and receive color-focused husbandry guidance. It is suited for recurring checks where white-balance reference, side-view capture, and species subtype context are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish images or videos, report history, and a stable agent identity may be sent to the provider's cloud service.

Mitigation: Install only when this data sharing is acceptable, avoid sensitive media, and review provider retention and access controls before use.

Risk: The package may default to insecure HTTP endpoints for some service URLs.

Mitigation: Require HTTPS-only endpoints in configuration before executing analysis or history queries.

Risk: The skill can automatically create or reuse a persistent identity and may store tokens locally.

Mitigation: Review identity creation and token-storage behavior, avoid silent account creation for one-off analysis, and rotate or delete stored credentials when no longer needed.

Risk: Color-based findings may be mistaken for veterinary diagnosis or treatment advice.

Mitigation: Use results as color and husbandry support only; do not provide disease diagnoses, medication names, dosages, or treatment plans.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [Analysis API Reference](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text, with optional file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HSV metrics, species-baseline comparisons, vibrancy scores, trend summaries, recommended actions, and report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

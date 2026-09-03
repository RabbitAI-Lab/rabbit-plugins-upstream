## Description:

Detects fish flashing and scraping behavior from fixed aquarium video, counts abnormal contact frequency, and produces ectoparasite risk warnings with observation guidance rather than a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External aquarists, aquarium operators, aquaculture teams, and agents use this skill to analyze fixed-camera fish videos for repeated flashing or scraping behavior and to generate structured warning reports. The skill supports early risk triage, history lookup, and user-facing recommendations to observe fish condition and seek professional veterinary microscopy when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium videos or URLs are sent to the Life Emergence backend for analysis.

Mitigation: Install only when that data sharing is acceptable and review backend permissions, retention, and user consent requirements before deployment.

Risk: The skill silently creates or reuses an internal account identity, queries cloud report history, and stores account tokens locally.

Mitigation: Prefer an updated release that makes cloud history lookup opt-in, documents permissions and retention, and provides a way to clear stored identity and tokens.

Risk: Behavioral warnings could be mistaken for a specific parasite diagnosis or treatment plan.

Mitigation: Keep outputs framed as ectoparasite risk signals, avoid medication or dosage guidance, and direct users to close observation and professional veterinary microscopy for confirmation.

Risk: Poor video quality, blind spots, low frame rate, species baseline differences, feeding, breeding, stress, or water-temperature changes can cause false alerts.

Mitigation: Require adequate camera coverage, lighting, frame rate, and tracking quality; return an unreliable-signal result when those conditions are not met and account for species and context baselines.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-flashing-scraping-detection-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with status messages and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include friction event counts, duration, affected fish counts, alert level, recommended observation actions, and history-report links.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes images or videos of ornamental fish to estimate color vibrancy against species-specific baselines and return a structured report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and ornamental fish operators use it to review fish color measurements and trends from images or video. Its guidance treats scores as color indicators, not disease diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marks the skill suspicious because it reports broad account, credential, and remote-service behavior that does not clearly match fish color analysis; the scan is partial and did not assess all referenced material.

Mitigation: Before use, clarify and limit account and credential access, confirm the destinations and purpose of remote requests and media uploads, and review the unresolved reference. Avoid submitting media or credentials until these flows are understood.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Guidance]

**Output Format:** [Structured report with color measurements, vibrancy score, trends, alert level, recommendations, and disclaimer; JSON by default.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image and video assessment depends on reliable white balance, a visible fish profile, and a species-specific baseline.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

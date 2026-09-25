## Description:

Measures fish fry body length and growth rate from periodic images or videos that include a known-size reference object, then returns structured growth statistics, curves, report links, and management-oriented alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External aquaculture operators, ornamental fish breeders, lab users, and agents use this skill to analyze fry tank media with a reference object, estimate body length and growth rate, review historical measurements, and decide whether feeding, grading, or water-quality checks are warranted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fish tank images or videos, media URLs, and history queries may be sent to configured lifeemergence.com cloud services.

Mitigation: Use the skill only where users have authorized cloud processing, avoid sensitive media, and review retention, deletion, and report-access controls before production use.

Risk: The skill can silently create or reuse identity and link uploads and history queries to that identity.

Mitigation: Review local identity and token storage behavior, especially for shared farm, lab, or workstation environments, and separate or delete records when operators change.

Risk: Growth measurements can be misleading if the reference object, camera angle, image clarity, or fish posture is unsuitable.

Mitigation: Require a known-size reference object in the same plane, strict overhead capture, clear media, and human review of unreliable or high-impact outputs before changing husbandry practices.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis output with structured measurements, growth statistics, recommendations, history listings, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the analysis output to a user-specified file and may query cloud-hosted history for the resolved user identity.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

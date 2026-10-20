## Description:

Analyzes cage images or videos for waste coverage and cleanliness, then provides cleaning alerts and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet boarding, retail, veterinary, and breeding staff use cage images or videos to assess waste coverage, identify cleaning needs, and review previous reports. Results support hygiene monitoring, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cage images, videos, or media URLs are sent to a third-party cloud service.

Mitigation: Obtain user approval before submission and confirm the service's data-handling terms.

Risk: The skill automatically manages an identity and stores account tokens in a workspace SQLite database.

Mitigation: Keep the skill directory private and restrict access to its workspace data.

Risk: Cloud history queries can expose prior cage-cleanliness reports.

Mitigation: Require explicit approval for history retrieval and limit access to authorized users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)
- [Cage cleanliness API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports, Markdown history tables, or JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleanliness scores, cleaning alerts, recommendations, and report links.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

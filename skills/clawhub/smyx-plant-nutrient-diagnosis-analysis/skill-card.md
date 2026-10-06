## Description:

Analyzes plant leaf images or videos to suggest likely nutrient deficiencies, confidence levels, and fertilization directions, with access to past reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, growers, and agricultural teams use leaf images or videos to explore possible nutrient deficiencies and review prior diagnoses before deciding whether to seek soil testing or agronomic advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and report queries are sent to the publisher's cloud service.

Mitigation: Review what may be shared and avoid submitting sensitive images or account information without authorization.

Risk: The skill silently creates or reuses a user identity and stores user records and service tokens locally.

Mitigation: Review local storage and access controls before installation, especially on shared workspaces.

Risk: Similar leaf symptoms or poor images can produce uncertain diagnoses and inappropriate fertilizer decisions.

Mitigation: Treat results as preliminary; confirm with plant context, soil testing, or an agronomic expert before fertilizing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown diagnostic reports or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include likely deficiencies, confidence levels, suggested actions, and report links; history requests return a report list.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

## Description:

Analyzes classroom and playground video for children's social interactions and produces interaction summaries and heatmaps for educators.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and early-education staff use the skill to review interaction frequency, duration, and participation among children in group video, with results intended as educational observations rather than diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's classroom or playground media and report queries are sent to remote services.

Mitigation: Obtain parent or guardian and school authorization; confirm the service's retention, deletion, and access controls before use.

Risk: Automatic identity setup and locally stored tokens may expose report access.

Mitigation: Review identity and token storage, restrict report access, and adopt safer credential storage before deployment.

Risk: Social-interaction observations could be mistaken for developmental or autism diagnoses.

Mitigation: Treat findings as non-diagnostic educational observations and require professional review for developmental concerns.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-social-interaction-analysis-analysis)
- [Social interaction analysis API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON; Markdown tables and report links for history queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interaction counts, durations, heatmap links, and report export links.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; artifact frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

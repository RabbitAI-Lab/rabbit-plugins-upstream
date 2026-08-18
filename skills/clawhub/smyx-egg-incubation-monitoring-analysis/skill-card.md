## Description:

Analyzes turtle or snake egg images, videos, or URLs to assess shell color, blood streaks, vascular signs, embryo silhouette, development stage, and incubation report outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile breeders, smart incubator operators, and breeding-management app developers use this skill to analyze turtle or snake egg media and produce incubation progress reports. It is intended to support visual monitoring, historical report review, and non-invasive recommendations rather than replace species-specific husbandry manuals or professional review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud processing can send uploaded media or supplied URLs to remote service endpoints.

Mitigation: Use only with media that is appropriate for the configured service, and verify the API URLs before running the skill.

Risk: The skill can associate analyses with an internal identity and query historical reports.

Mitigation: Review account handling and report-retention expectations before installation, especially in shared workspaces.

Risk: Local workspace storage can contain account records or remote tokens.

Mitigation: Treat the workspace data directory as sensitive and remove stored credentials or records when decommissioning the skill.

Risk: Visual egg-development classifications may be wrong or unreliable when image quality, lighting, species context, or handling history is incomplete.

Mitigation: Require clear non-invasive imagery, species and incubation context, and human review before acting on important breeding decisions.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with classifications, alert level, recommended actions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file and can query cloud-hosted historical incubation reports.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

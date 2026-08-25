## Description:

Analyzes pet full-body images or videos through server-side APIs to estimate breed or body type and fur density, then returns a drying temperature and time curve for pet drying devices, grooming salons, or smart care workflows; it is not medical advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, grooming operators, and smart pet-care device teams use this skill to submit pet media or URLs for breed/body-type and fur-density analysis and receive drying temperature/time recommendations for device or care workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or media URLs are sent to the Life Emergence/SMYX backend for analysis.

Mitigation: Use the skill only with user-approved, non-sensitive pet media and in environments where outbound submission to that backend is acceptable.

Risk: The skill can create or reuse an internal account identity and store local tokens.

Mitigation: Avoid shared workspaces and review token storage, retention, and cleanup practices before installation.

Risk: History queries can return cloud records linked to the current account identity.

Mitigation: Limit history-list usage to authorized contexts and review returned report links before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-adaptive-pet-drying-temperature-analysis)
- [Pet adaptive drying API documentation](artifact/references/api_doc.md)
- [SMYX analysis API error-code reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [markdown, json, guidance]

**Output Format:** [Markdown or JSON structured analysis report with recommended temperature and time curve, safety notes, and optional report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the report to a file when an output path is provided.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

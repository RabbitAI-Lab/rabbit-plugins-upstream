## Description:

Detects plant growth stages from plant images or video by sending media for cloud analysis and returning the phenological stage, confidence, care guidance, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze plant images or videos from smart pots, home grow boxes, greenhouses, or plant factories and identify the current growth stage. It can also retrieve cloud-hosted historical plant growth reports associated with the skill's internal user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report queries are handled through under-disclosed remote endpoints.

Mitigation: Use a dedicated workspace and account, inspect or change endpoint configuration before running, and avoid private greenhouse or home imagery unless the publisher clarifies endpoint ownership, retention, and access controls.

Risk: The skill silently creates or reuses local identities and persists account or token state.

Mitigation: Run in an isolated environment, review local state before and after use, and avoid sharing the workspace with unrelated users or projects.

Risk: Growth-stage assessments and care suggestions may be wrong for unclear images, transitional stages, or plant-specific requirements.

Mitigation: Treat results as reference guidance only, confirm with plant-specific context, and do not use outputs as the sole basis for agricultural decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [JSON or Markdown report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results include plant growth stage, confidence, general care guidance, and report links; history mode returns a Markdown table from cloud report data.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

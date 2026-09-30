## Description:

Analyzes plant images or videos to identify growth stages and provide structured reports for agricultural decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers and their agents use plant images or videos to identify growth stages, review analysis reports, and retrieve past reports for crop-management decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and an internal user identifier are sent to lifeemergence.com services.

Mitigation: Review the service's data handling before sharing images or videos, and use only media approved for cloud processing.

Risk: The skill silently creates or reuses identities and stores reusable tokens and report-history linkage in the local workspace.

Mitigation: Review before installing; avoid sensitive identity files in the workspace until the publisher clarifies retention, deletion and permission boundaries.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown report list; optional saved file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes growth-stage results, recommendations and report links; can retrieve cloud report history.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; bundled SKILL.md says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

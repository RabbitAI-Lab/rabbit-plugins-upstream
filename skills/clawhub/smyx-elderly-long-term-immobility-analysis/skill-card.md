## Description:

Analyzes fixed-camera home video for solo-living elder activity and produces long-term no-activity alerts when configured inactivity thresholds, default 12 hours, are exceeded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, community elder-care operators, and smart-home integrators use this skill to analyze elder-care camera video or video URLs for prolonged inactivity and produce structured alerts, report links, and history reports. It is an auxiliary monitoring tool and does not provide medical diagnosis or rescue instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive elder-care home video or video URLs may be sent to LifeEmergence services for analysis.

Mitigation: Use only with consent from the monitored person or lawful representative, avoid bathroom or bedroom cameras where possible, and confirm that service-side handling meets the deployment's privacy requirements.

Risk: The skill can create or reuse local account identity state and retain tokens or default identity data in the workspace.

Mitigation: Restrict workspace access, review the local data store before and after use, and delete retained identity or token state when it should not persist.

Risk: Account-linked history reports can expose sensitive monitoring results.

Mitigation: Limit who can request report history, treat generated report links as sensitive, and audit access before enabling shared or unattended use.

Risk: Long-term inactivity alerts are safety-relevant but are based on visual activity analysis rather than medical assessment.

Mitigation: Treat alerts as prompts for immediate human verification by phone or in person, and do not use the skill as a medical diagnosis or emergency response substitute.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-long-term-immobility-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content, command examples, alert fields, history tables, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, history listing, optional output file writing, and basic/standard/json detail levels; documented media constraints include mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

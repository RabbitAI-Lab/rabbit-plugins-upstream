## Description:

Monitors infant behavior via visual AI, automatically identifying high-risk actions like rolling over, mouth/nose obstruction, climbing, or falling from bed, and triggers instant safety warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to analyze infant activity photos or videos for safety risks such as mouth or nose obstruction, prone sleep posture, climbing, crib escape, and fall risk. The skill produces safety warnings, care suggestions, report links, and cloud-hosted history lookups for prior analyses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive infant photos, videos, and account-linked analysis history through a remote service.

Mitigation: Install only when remote processing and retention are acceptable, and review the publisher's service handling before use.

Risk: The security review flags shipped configuration and credential handling as requiring review before installation.

Mitigation: Require HTTPS-only production endpoints, remove default development HTTP configuration, and avoid storing reusable tokens in a plain workspace database.

Risk: Analysis results may be affected by video clarity, lighting, and camera stability, and are not a replacement for caregiver supervision.

Mitigation: Use the reports as safety support only, capture clear stable media, and maintain real-time caregiver monitoring.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant safety monitoring API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown safety reports, JSON analysis payloads, report links, and shell command invocations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports mp4, avi, and mov inputs up to 10 MB; history reports are retrieved from the remote service and formatted for the user.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata; artifact frontmatter reports 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

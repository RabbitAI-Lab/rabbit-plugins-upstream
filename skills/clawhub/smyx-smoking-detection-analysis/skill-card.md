## Description:

Detects smoking behavior in images, videos, and video streams, then returns structured analysis and violation alerts for smoking-control management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Facility, campus, community, and workplace safety teams can use this skill through an agent to analyze submitted media for possible smoking violations, review structured detection results, and query report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files or URLs may be processed by external lifeemergence.com services.

Mitigation: Use the skill only when that data flow is acceptable, and avoid submitting sensitive local files or internal-only URLs.

Risk: The skill may silently create or reuse a persistent cloud-linked identity and store tokens or profile data.

Mitigation: Review identity handling, token storage, and report-retention behavior before installation or deployment.

Risk: Server security evidence marks the release as suspicious.

Mitigation: Review and scan the skill before installing, and deploy it only after accepting the documented media-processing and identity-linking behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured analysis summaries, JSON detail output, report lists, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; analysis accepts documented image, video, local file, and URL inputs.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter lists 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

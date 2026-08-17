## Description:

AI-powered UV disinfection safety monitor for pets that analyzes camera images or videos to detect pet presence, UV lamp activity, combined exposure risk, alert recommendations, and event reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet-care operators, and smart-home developers use this skill to analyze indoor UV disinfection footage, identify whether pets are exposed while UV equipment is active, and produce safety alerts, recommendations, and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor pet videos or video URLs may be sent to configured remote analysis services.

Mitigation: Review endpoint configuration and publisher privacy documentation before using sensitive household footage.

Risk: The skill may create and reuse persistent local identity or token state.

Mitigation: Run in an isolated environment and review account-linkage, retention, and deletion controls before deployment.

Risk: Default configuration includes development HTTP endpoints and under-scoped remote APIs.

Mitigation: Confirm production HTTPS endpoints, credentials, and network routing before commercial use.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with risk status, recommendations, and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call remote analysis APIs for video processing and historical report retrieval.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

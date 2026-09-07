## Description:

Analyzes driver videos to identify unsafe driving behaviors and return structured reports with safety observations, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to evaluate driver video or image inputs for fatigue, distraction, seatbelt use, posture, and other unsafe driving behavior patterns. It can also retrieve cloud-hosted historical driving analysis reports for the internally associated account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos, report contents, and historical report requests may be sent to external cloud services.

Mitigation: Use only non-sensitive test media until the publisher documents data destinations, retention, access controls, and consent requirements.

Risk: The skill silently manages account identity and may store reusable tokens in a local workspace database.

Mitigation: Install only after reviewing account-handling behavior; avoid shared workspaces and remove local credentials or databases after testing.

Risk: Development HTTP endpoints are present in the artifact configuration.

Mitigation: Confirm development configuration is disabled and HTTPS production endpoints are enforced before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text with structured analysis content, safety recommendations, and report links; JSON detail output is also supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save the returned report content to a user-specified output file; supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

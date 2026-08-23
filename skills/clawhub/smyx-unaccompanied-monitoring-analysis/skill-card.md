## Description:

Determines when elderly people living alone have no interaction or visitors for extended periods, and actively pushes care reminders to family members, suitable for remote care scenarios for elderly people living alone at home.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-operations teams use this skill to analyze home monitoring media for prolonged lack of interaction or visitors and to produce care reminders, structured results, historical report listings, and report links for family or community follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home monitoring images, videos, or URLs may be sent to the configured remote backend.

Mitigation: Use only media for which the monitored person and anyone captured on camera have given appropriate consent, and verify the backend endpoint and retention policy before installation.

Risk: The skill can silently create or reuse a local workspace identity and authentication tokens.

Mitigation: Review identity and token handling in the target workspace before deployment, and run the skill only in an environment where that automatic association is expected.

Risk: Automated unattended-care analysis can miss events or generate misleading reassurance or alerts.

Mitigation: Treat results as care-reminder support only, and keep human check-ins, professional care processes, and emergency procedures in place.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-unaccompanied-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and JSON text from CLI/API responses, including structured analysis results, historical report listings, recommendations, and report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local media files or media URLs; local file validation is configured for mp4, avi, and mov files up to 10 MB.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact SKILL.md frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

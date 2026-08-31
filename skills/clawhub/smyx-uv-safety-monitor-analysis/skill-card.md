## Description:

This skill sends pet or home video inputs to the publisher's cloud service to analyze whether pets appear in a UV disinfection area and returns structured risk reports, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit UV disinfection-area pet videos or video URLs for cloud analysis, receive structured monitoring results, and query historical reports. It is intended as safety-support guidance, not as a standalone medical or automatic UV-lamp shutoff system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home video, video URLs, and report queries are sent to the publisher's cloud service.

Mitigation: Use the skill only with media and URLs that are appropriate to share with the publisher's service.

Risk: The skill makes safety-critical and automatic-control claims that are not supported by the local code evidence.

Mitigation: Treat results as advisory and keep independent UV-lamp controls, supervision, and emergency procedures in place.

Risk: The skill can create and persist a local identity with stored tokens.

Mitigation: Review local identity and token storage before deployment and clear stored credentials when the skill should no longer retain access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-formatted structured analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and exported report image URLs; accepts local video files or video URLs.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

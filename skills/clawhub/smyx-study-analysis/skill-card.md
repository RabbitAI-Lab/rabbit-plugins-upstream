## Description:

Analyzes child or student study videos to identify learning behaviors and produce structured reports with family education improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and caregivers use this skill to submit child or student learning videos for behavior, focus, posture, habit, and risk analysis. The skill returns structured reports, education suggestions, and history/report links for family education review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child or student videos, video URLs, account-linked identifiers, and report history are sent to the publisher's cloud service.

Mitigation: Use only with appropriate consent and after reviewing the publisher's documentation for account creation, token storage, data retention, and deletion behavior.

Risk: The security evidence flags under-secured cloud and authentication flows, including default plaintext HTTP development endpoints.

Mitigation: Require HTTPS-only endpoints, host allowlisting, and review of credential attachment behavior before installation or deployment.

Risk: Learning behavior analysis reports may be mistaken for professional educational or psychological assessment.

Mitigation: Treat results as family education reference material and seek qualified professional support for serious learning or behavioral concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report, with report history rendered as Markdown from API data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include learning behavior scores, risk warnings, family education suggestions, and report export links.]

## Skill Version(s):

1.0.16 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
